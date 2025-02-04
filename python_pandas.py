#! /usr/bin/env python3

import pprint
import pandas as pd
class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def data_loader(self):
        df = pd.read_csv(self.file_path)
        # print the first 5 rows of the dataframe
        return df
    def data_info(self, df):
        # print(df.describe())
        # print(df.info())
        # print(df.shape)

        missing_values = self.missing_values(df)
        fill_missing_values = self.fill_missing_values(df)
        # if missing_values == 0:
        #     print("No missing values")
        # else:
        #     print("Missing values: ", missing_values)
        #     print("Filled missing values: ", fill_missing_values)
    
    def missing_values(self, df):
        # get the number of missing values
        df_missing=df.isnull().sum()
        # get the percentage of missing values
        return df.isnull().sum()
    # fill missing values
    def fill_missing_values(self, df):
        # fill missing values with mean
        df.fillna(df.mean(), inplace=True)
        count_filled = df.isnull().sum()
        return df, count_filled
    # fill missing values with median
    def fill_missing_values_median(self, df):
        df.fillna(df.median(), inplace=True)
        count_filled = df.isnull().sum()
        return df, count_filled
    
    # fill missing values with mode
    def fill_missing_values_mode(self, df):
        df.fillna(df.mode(), inplace=True)
        count_filled = df.isnull().sum()
        return df, count_filled # return the dataframe and the count of filled missing values
    
    # remove outliers
    def remove_outliers(self, df):
        df.drop_duplicates(inplace=True)
        count_outliers = df.duplicated().sum()
        return df, count_outliers # return the dataframe and the count of outliers

    # sorting, filtering, grouping, and aggregating
    def sorting(self, df):
        sorted_df = df.sort_values(by='median_house_value', ascending=False)
        sorted_df.head(10)
        # pprint.pprint(sorted_df)
        return sorted_df
    
    def filtering(self, df):
        filtered_df = df[df['median_house_value'] > 200000]
        filtered_df.head(10)
        # pprint.pprint(filtered_df)
        return filtered_df
    # filtering
    #grouping
    def grouping(self, df):
        grouped_df = df.groupby('Neighborhood').sum()
        grouped_df.head(10)
        # pprint.pprint(grouped_df)
        return grouped_df
    #aggregating
    def aggregating(self, df):
        aggregated_df = df.groupby('median_house_value').agg(['sum', 'mean', 'median', 'std', 'min', 'max'])
        aggregated_df.head(10)
        pprint.pprint(aggregated_df.head(10))
        return aggregated_df


if __name__ == "__main__":  
    file_path = 'datasets/housing/housing.csv'
    data_loader = DataLoader(file_path)
    df= data_loader.data_loader()
    # data_loader.data_info(df)
    # data_loader.missing_values(df)
    # data_loader.sorting(df)
    # data_loader.filtering(df)
    # data_loader.grouping(df)
    data_loader.aggregating(df)
    # data_loader.remove_outliers(df)
    # data_loader.fill_missing_values(df)
    # data_loader.fill_missing_values_median(df)
    # data_loader.fill_missing_values_mode(df)

