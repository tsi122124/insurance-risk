

def calculate_loss_ratio(df):
    return (
        df["TotalClaims"].sum() /
        df["TotalPremium"].sum()
    )


def add_margin(df):
    df = df.copy()
    df["Margin"] = (
        df["TotalPremium"] -
        df["TotalClaims"]
    )
    return df


def missing_value_summary(df):
    return (
        df.isnull()
          .sum()
          .to_frame("MissingCount")
          .assign(
              MissingPercent=lambda x:
              round(
                  x["MissingCount"] /
                  len(df) * 100,
                  2
                   )
                  )
          .sort_values(
              "MissingPercent",
              ascending=False
                      )
    )


def claim_frequency(df):
    return (
        df["TotalClaims"] > 0
    ).mean()
