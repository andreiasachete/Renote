import csv


def read_authors_list(input_file_path):
    with open(input_file_path, mode="r", encoding="utf-8") as file:
        authors = [row[0] for row in csv.reader(file)]

    return authors


def main():
    # Reading the input dataset
    authors_list = read_authors_list("nodes.csv")

    # Creating a preliminary data structure to count the number of papers per author
    authors_metadata = {}
    for entry in authors_list:
        # Creating counter for the author if it wasn't created yet
        if entry not in authors_metadata:
            authors_metadata[entry] = 0

        # Incrementing the author counter
        authors_metadata[entry] += 1

    # Creating an organized data structure for the authors and their papers count
    parsed_dataset = []
    for author_name, number_of_papers in authors_metadata.items():
        parsed_dataset.append(
            {
                "Nome": author_name,
                "Artigos": number_of_papers,
            }
        )

    # Sorting the authors metadata by their number of papers
    parsed_dataset = sorted(
        parsed_dataset,
        key=lambda author_metadata: author_metadata["Artigos"],
        reverse=True,
    )

    # Displaying the results
    for item in parsed_dataset:
        print(item)

    # Exporting the results to a CSV file
    with open("numero_de_artigos_por_autor.csv", mode="w", newline="") as file:
        # Creating a DictWriter object with fieldnames from the dictionary keys
        writer = csv.DictWriter(file, fieldnames=parsed_dataset[0].keys())

        # Writing the CSV header
        writer.writeheader()

        # Writing the CSV rows
        for row in parsed_dataset:
            writer.writerow(row)


if __name__ == "__main__":
    main()
