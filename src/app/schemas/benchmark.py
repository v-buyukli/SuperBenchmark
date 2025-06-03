from datetime import datetime

from pydantic import BaseModel


class BenchmarkResult(BaseModel):
    request_id: str
    prompt_text: str
    generated_text: str
    token_count: int
    time_to_first_token: int
    time_per_output_token: int
    total_generation_time: int
    timestamp: datetime


class BenchmarkAverageStats(BaseModel):
    avg_token_count: float
    avg_time_to_first_token: float
    avg_time_per_output_token: float
    avg_total_generation_time: float
