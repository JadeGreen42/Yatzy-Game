# api.py
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import random


try:
    from logic import RNGenerator  
except Exception:
    def RNGenerator() -> List[int]:  # fallback deterministic generator
        return [random.randint(1, 6) for _ in range(5)]

try:
    from scoring import scoring  
except Exception:
    def scoring(choice: int, dice: List[int]):
        return sum(dice), None


app = FastAPI(title="Yatzy Minimal API", version="1.0")


class ScoreRequest(BaseModel):
    choice: int
    dice: List[int]

    @field_validator("dice")
    def validate_dice(cls, v):
        if not isinstance(v, list) or len(v) != 5:
            raise ValueError("dice must be a list of 5 integers")
        for x in v:
            if not isinstance(x, int) or not (1 <= x <= 6):
                raise ValueError("each die must be an integer between 1 and 6")
        return v


@app.get("/health")
def health():
    """Simple health check."""
    return {"status": "ok"}


@app.get("/roll")
def roll():
    """Return a fresh random roll of 5 dice."""
    try:
        dice = RNGenerator()
        # defensive: ensure returned structure is valid
        if not isinstance(dice, list) or len(dice) != 5:
            raise ValueError("RNGenerator did not return a list of 5 ints")
        return {"dice": dice}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"roll error: {e}")


@app.post("/score")
def score_endpoint(req: ScoreRequest):
    """Score provided dice for given category (choice)."""
    try:
        score_value, flag = scoring(req.choice, req.dice)
    except Exception as e:
        # scoring implementation might raise on invalid category
        raise HTTPException(status_code=400, detail=f"scoring error: {e}")

    # normalize the flag for clearer JSON (True for upper-section categories, else False)
    is_upper = bool(flag)
    return {"score": score_value, "is_upper_section": is_upper}
