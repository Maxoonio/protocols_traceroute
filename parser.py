from ip_information import data

def result_function(ips):
    with open("out.txt", "w", encoding="utf-8") as file:
        file.write("| Number | IP Address          | AS       | Country   | Provider             |\n")
        file.write("|--------|---------------------|----------|-----------|----------------------|\n")

        for index, ip in enumerate(ips):
            ip, as_number, country, provider = data(ip)

            line = (
                f"| {index:<6} | {ip:<19} | {as_number:<20} | "
                f"{country:<9} | {provider:<20} |\n"
            )
            file.write(line)