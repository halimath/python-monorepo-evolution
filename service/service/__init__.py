from diceroller import Roll
from fastapi import FastAPI, Response
from pydantic import BaseModel, Field

class RollRequest(BaseModel):
    """Request made to the /roll endpoint to execute the diceroller expression."""
    expr: str = Field(
        title='The diceroller expression',
        description='The diceroller expression to execute', 
        examples=['d20+3', '3d8+5']
    )

class RollResponse(BaseModel):
    expr: str = Field(
        title='The roll expression',
        description='The diceroller expression that has been executed'
    )
    result: int = Field(
        title='The overall result',
        description='The total result value of the roll'
    )
    natural_result: int = Field(
        title='The natural result',
        description='The natural result, i.e. all dice rolls added together but w/o applying any modifier'
    )

app = FastAPI()

@app.post('/api/v1/roll')
async def roll(r: RollRequest, response: Response) -> RollResponse:
    """Execute a diceroller expression and return the result."""
    response.headers['Cache-Control'] = 'no-store, no-cache'
    roll = Roll(r.expr)
    return RollResponse(expr=r.expr, result=roll.value, natural_result=roll.natural)
