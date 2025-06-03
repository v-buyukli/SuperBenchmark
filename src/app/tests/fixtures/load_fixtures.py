import json
from pathlib import Path

import aiofiles

from src.app.schemas.benchmark import BenchmarkResult


FIXTURES_DIR = Path(__file__).parent


async def load_test_benchmarks() -> list[BenchmarkResult]:
    file_path = FIXTURES_DIR / 'test_database.json'
    async with aiofiles.open(file_path, mode='r', encoding='utf-8') as f:
        raw = json.loads(await f.read()).get('benchmarking_results', [])
    return [BenchmarkResult(**item) for item in raw]
