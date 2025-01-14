from bs4 import BeautifulSoup
import requests
import smtplib
url = "https://www.amazon.fr/Apple-Circum-auriculaire-r%C3%A9duction-Transparence-personnalis%C3%A9/dp/B0DGJ74WP3/ref=sr_1_29?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1B89MNZKUCN3&dib=eyJ2IjoiMSJ9.z0Ttg8Rv5Okyo1HHKMlUUtPdZ2hor_WXgGzgWsrvTfOdiCduL247vkVW4TcuU9Gp6s706WhTOFttDukJGOecBgPbeyYvz4IdiPY6cvH7tkw4HPx6p6cSjpixs1DKM_-iE4ekfh1tuo6U0mtnLWViKWfQ-M_XNaijuJ5aCMhuV79zesV1CubQABzFNs5BpXzH8wmqjjPAcSrwN-cocSOAXoCgjcChiVG9LE5PTP9dCNs1VewqG77Yz_EVegNAjEyN4W9UXI5T2pFyk-4YKo7e6phQGBhkvuLdyx2tViOaVT_w38FoLxFOHRmvbfvHfc19A9GrTqrW_LXhZkKcxHmb8xZM1R4lLw0gYQxSY09l2Sna23I3BgCbvwCpjQdxWUqzR1rE_l0NqddjWI_ad27LbSMlKaGqogMcS3ImtptXj8180AWYTSv6IQJy9dQvsezg.RB3sdB-_5PZujuGJH6SMYpTSDlqUbYKkZmSLNwS3KRI&dib_tag=se&keywords=apple%2Becouteur&nsdOptOutParam=true&qid=1736897688&sprefix=apple%2Becouteur%2Caps%2C183&sr=8-29&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
title_cible = soup.find("h1", id="title")
title = title_cible.text.strip(" ")
price_attr = soup.find(class_="a-offscreen")

price = float(price_attr.getText().split("€")[0].replace(",", "."))


# Send mail if the price is < 100 €
if price < 100:
    with smtplib.SMTP_SSL("smtp.gmail.com") as mail:
        mail.login("<EMAIL>", "<PASSWORD>")
        mail.sendmail(
            from_addr="<EMAIL>",
            to_addrs="<EMAIL>",
            msg=f"The price is low !\n\n The price for {title} is {price}€ now"
        )
