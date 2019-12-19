import os
import glob
import json
import pandas as pd

from settings import AIR_DIRECTORY, AIR_TYPES


def concatenate_air_results():
    main_df = []
    for airtype in AIR_TYPES:
        path = os.path.join(AIR_DIRECTORY, airtype)
        files = glob.glob(path + "/*.txt")
        for filepath in files:
            with open(filepath) as f:
                datas = json.loads(f.read())
                df = pd.DataFrame(datas)
                df = df.rename(columns=df.iloc[0]).drop(df.index[0])
                date = filepath.split("-")[1].split(".")[0]  # TODO : sérialiser
                df["date"] = date
                main_df.append(df)

    data = pd.concat(main_df, ignore_index=True, axis=0)
    data["Latitude"] = data["Latitude"].astype(float)
    data["Longitude"] = data["Longitude"].astype(float)
    return data
