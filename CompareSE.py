import json
import csv


def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        file.close()
    return data


def load_queries():
    with open('Data/DDGQuery.txt', 'r') as file1:
        queries = file1.readlines()
        res = [x.strip().strip('\n') for x in queries]
        file1.close()
    return res


class CompareSE:

    def __init__(self, ddg, google, query):
        self.ddg = ddg
        self.google = google
        self.queries = query

    def compare_search_engine(self):
        total_overlap = 0
        total_percent_overlap = 0
        total_rho = 0
        comparision = [['Queries,', 'Number of Overlapping Results,', 'Percent Overlap,', 'Spearman Coefficient']]

        for query in self.queries:
            set_google = set(self.google[query])
            set_ddg = set(self.ddg[query])
            common = list(set_ddg.intersection(set_google))
            i = []
            j = []
            if common:
                for link in common:
                    i.append(self.google[query].index(link))
                    j.append(self.ddg[query].index(link))
                d = [x1 - x2 for (x1, x2) in zip(i, j)]
                d_square = [x * x for x in d]
                d_square_sum = sum(d_square)
                overlap = len(d)
            else:
                d_square_sum = 0
                overlap = 0

            percent_overlap = overlap/10*100

            if overlap == 0:
                rho = 0
            elif overlap == 1:
                if d_square_sum == 0:
                    rho = 1
                else:
                    rho = 0
            else:
                rho = 1 - ((6 * d_square_sum)/(overlap * (overlap ** 2 - 1)))

            total_overlap += overlap
            total_percent_overlap += percent_overlap
            total_rho += rho

            comparision.append([query + ',', str(overlap) + ',', str(percent_overlap) + ',', str(rho)])

        avg_overlap = total_overlap/len(self.queries)
        avg_percent_overlap = total_percent_overlap/len(self.queries)
        avg_rho = total_rho/len(self.queries)
        comparision.append(["Averages,", str(avg_overlap) + ',', str(avg_percent_overlap) + ',', str(avg_rho)])

        return comparision


if __name__ == "__main__":
    ddg_data = load_data('hw1.json')

    google_data = load_data('Data/Google_Result4.json')
    query_data = load_queries()

    comp = CompareSE(ddg_data, google_data, query_data)
    csv_result = comp.compare_search_engine()
    print(csv_result)

    with open('hw1.csv', 'w+') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(csv_result)
        f.close()
