import os
import pyterrier as pt


def create_index():
    # create index
    index_path = "./index"
    if not os.path.exists(index_path):
        indexer = pt.FilesIndexer(index_path)
        files = ["./scraped_documents/" + file for file in os.listdir("scraped_documents")]
        index_ref = indexer.index(files)
        index = pt.IndexFactory.of(index_ref)
        print(index.getCollectionStatistics().toString())


if __name__ == "__main__":
    if not pt.started():
        pt.init()

    create_index()
