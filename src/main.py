import polars


def main():
    df = (
        polars.scan_csv("./data/webchamame_20251102172307.csv")
        .filter(polars.col("品詞").str.contains("名詞"))
        .group_by(polars.col("書字形（＝表層形）"))
        .len(name="count")
        .sort(by=polars.col("count"), descending=True)
        .collect()
    )

    for [wordform, count] in df.filter(polars.col("count") >= 10).iter_rows(): # pyright: ignore[reportAny]
        print(f"A noun '{wordform}' is used {count} times")


if __name__ == "__main__":
    main()
