# -*- coding: utf-8 -*-
"""Google Data Analytics: data structures in Python (Module 4 part 1).

Lists, tuples, dictionaries, and sets applied to two real datasets:
Titanic train.csv and EPA air quality c2_epa_air_quality.csv.
Saves charts and findings.
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(BASE, "charts")
DATA = os.path.join(BASE, "data")

plt.rcParams.update({"figure.dpi": 130, "font.size": 10})


def savefig(name, title, xlabel="", ylabel=""):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS, name))
    plt.close()


def county_counter(df, county, state):
    mask = (df["county_name"] == county) & (df["state_name"] == state)
    return int(mask.sum())


def main():
    findings = {}

    print("== Lists dan tuples: Titanic ==")
    t = pd.read_csv(os.path.join(DATA, "train.csv"))
    names = t["Name"].tolist()
    print("Jumlah penumpang:", len(names))
    print("Contoh nama:", names[0])

    # list of lists via comprehension: [nama, umur, selamat]
    passengers = [[row["Name"], row["Age"], row["Survived"]]
                  for _, row in t.iterrows()]
    print("Contoh list of lists:", passengers[0])

    # unpacking
    first = passengers[0]
    nama, umur, selamat = first
    print("Unpacking =", nama[:30], "| umur:", umur, "| selamat:", selamat)

    surv_by_class = t.groupby("Pclass")["Survived"].mean().round(3)
    print("Rata rata selamat per kelas:\n", surv_by_class)
    findings["survival_rate_by_class"] = {
        str(k): float(v) for k, v in surv_by_class.items()}
    findings["titanic_rows"] = len(t)

    plt.figure(figsize=(6, 3.8))
    plt.bar([str(k) for k in surv_by_class.index],
            surv_by_class.values, color="#1D4ED8")
    savefig("01_survival_kelas.png", "Rata Rata Selamat per Kelas (Titanic)",
            "Kelas", "Rata rata selamat")

    plt.figure(figsize=(6, 3.8))
    plt.hist(t["Age"].dropna(), bins=20, color="#0D9488", edgecolor="white")
    savefig("02_umur.png", "Distribusi Umur Penumpang Titanic",
            "Umur", "Jumlah")

    print("== Dictionaries dan sets: EPA air quality ==")
    aqi = pd.read_csv(os.path.join(DATA, "c2_epa_air_quality.csv"))
    print("Baris:", len(aqi), "| Kolom:", list(aqi.columns))

    # dictionary: jumlah pembacaan per state
    readings = aqi["state_name"].value_counts().to_dict()
    print("5 state terbanyak:", dict(list(readings.items())[:5]))
    findings["top_states"] = dict(list(readings.items())[:5])

    az = readings.get("Arizona", 0)
    print("Pembacaan di Arizona:", az)
    findings["arizona_readings"] = int(az)

    ca_mean = round(float(aqi.loc[aqi["state_name"] == "California",
                                 "aqi"].mean()), 2)
    print("Rata rata AQI California:", ca_mean)
    findings["california_mean_aqi"] = ca_mean

    # county_counter
    wc_pa = county_counter(aqi, "Washington", "Pennsylvania")
    print("Washington County PA:", wc_pa, "pembacaan")
    findings["washington_county_pa"] = wc_pa

    in_counties = sorted(aqi.loc[aqi["state_name"] == "Indiana",
                                 "county_name"].unique().tolist())
    in_counts = {c: county_counter(aqi, c, "Indiana") for c in in_counties}
    top_in = dict(sorted(in_counts.items(), key=lambda x: x[1],
                         reverse=True)[:5])
    print("Top county Indiana:", top_in)
    findings["indiana_top_counties"] = top_in

    # sets: county yang namanya dipakai di banyak state
    all_counties = aqi["county_name"].tolist()
    unique_counties = set(all_counties)
    county_states = aqi.groupby("county_name")["state_name"].nunique()
    shared = int((county_states > 1).sum())
    print("County unik:", len(unique_counties),
          "| dipakai di >1 state:", shared)
    findings["unique_counties"] = len(unique_counties)
    findings["shared_county_names"] = shared

    top_counties = aqi["county_name"].value_counts().head(10)
    plt.figure(figsize=(7, 4.2))
    plt.barh(top_counties.index[::-1], top_counties.values[::-1],
             color="#7C3AED")
    savefig("03_top_county.png", "10 County dengan Pembacaan Terbanyak",
            "Jumlah pembacaan", "")

    plt.figure(figsize=(6, 3.8))
    plt.bar(["unik", "nama dipakai ulang"],
            [len(unique_counties) - shared, shared],
            color=["#16A34A", "#F59E0B"])
    savefig("04_county_set.png", "County Unik vs Nama Dipakai Ulang",
            "", "Jumlah")

    with open(os.path.join(BASE, "findings.json"), "w") as f:
        json.dump(findings, f, indent=2, ensure_ascii=False)
    print("Selesai. Chart tersimpan di charts/.")


if __name__ == "__main__":
    main()
