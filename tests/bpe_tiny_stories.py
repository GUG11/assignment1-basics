# /usr/bin/time -l uv run python tests/bpe_tiny_stories.py
import time

from tests.adapters import run_train_bpe
from tests.common import FIXTURES_PATH
from tests.utils.logger import get_logger


logger = get_logger("tiny_stories")


if __name__ == "__main__":
    t_start = time.time()
    input_path = FIXTURES_PATH / "tinystories_sample_5M.txt"
    vocab, merges = run_train_bpe(
        input_path=input_path,
        vocab_size=10000,
        special_tokens=["<|endoftext|>"],
    )
    t_end = time.time()
    logger.info(f"Time taken: {t_end - t_start} seconds")
    longest_token = max(vocab.items(), key=lambda x: len(x[1]))
    logger.info(f"Longest token: {longest_token}")
