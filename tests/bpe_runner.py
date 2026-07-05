# /usr/bin/time -l uv run python tests/bpe_runner.py tinystories_sample_5M.txt
# /usr/bin/time -l uv run python tests/bpe_runner.py owt_train.txt -s 32000
import time
import argparse

from tests.adapters import run_train_bpe
from tests.common import FIXTURES_PATH
from tests.utils.logger import get_logger


logger = get_logger("tiny_stories")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str)
    parser.add_argument("-s", "--vocab_size", type=int, default=10000)
    args = parser.parse_args()
    t_start = time.time()
    input_path = FIXTURES_PATH / args.input_file
    vocab, merges = run_train_bpe(
        input_path=input_path,
        vocab_size=args.vocab_size,
        special_tokens=["<|endoftext|>"],
    )
    t_end = time.time()
    logger.info(f"Time taken: {t_end - t_start} seconds")
    longest_token = max(vocab.items(), key=lambda x: len(x[1]))
    logger.info(f"Longest token: {longest_token}")
