import concurrent.futures
import multiprocessing
import requests


def download_file(url, name):
    print(f"Started downloading {name}.jpg")
    response = requests.get(url)
    open(f"files/{name}.jpg", "wb").write(response.content)
    print(f"Download complete for {name}.jpg")

if __name__ == "__main__":

    url = "https://picsum.photos/2000/3000"

    ## Long way
    # processes = []
    # for i in range(5):
    #     # download_file(url, f"file{i}")  # normal process
    #     p = multiprocessing.Process(target=download_file, args=[url, f"file{i}"])
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()

    ## Short way
    with concurrent.futures.ProcessPoolExecutor() as executor:
        total_files = 5
        l = [f"file{i}" for i in range(total_files)]
        # executor.map(func, list of the 1st arg, list of 2nd arg, list of 3rd arg, ...)
        results = executor.map(download_file, [url] * total_files, l)
        for result in results:
            print(result)
