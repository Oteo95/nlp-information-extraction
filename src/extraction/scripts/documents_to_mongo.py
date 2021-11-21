import logging
import argparse
import pandas as pd

from extraction.process.preprocess_text import PreprocessDocs
from extraction.db.db_handler import MongoHandler

logger = logging.getLogger(__name__)


def run_load_dataset(raw_csv_path: str):
    raw_docs = pd.read_csv(raw_csv_path)
    if raw_docs is not None:
        process_docs = PreprocessDocs().get_mongo_documents(raw_docs)
        logger.info(process_docs)
        mh = MongoHandler()
        mh.delete_db()
        logger.info("Inserting documents in mongo.")
        mh.insert_documents(process_docs)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '--set',
        default='dividend_sample_moneyweb_co_za.csv',
        help='test, dev or train'
    )
    argparser.add_argument(
        '--directory',
        default='/workspace/data/dividends'
    )
    args = argparser.parse_args()
    raw_csv_path = f"{args.directory}/{args.set}"
    logging.info(f'Loading {args.set} documents...')
    run_load_dataset(raw_csv_path)
    logging.info('Finished')
