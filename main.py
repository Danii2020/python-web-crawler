# This is the main Python file where you import the 
# previous class and call all the methods in an interactive menu.
import crawler # import the crawler "module".
import pandas as pd # import the pandas library to save the data in an Excel file.
ycrawler = crawler.Crawler() # initialize the crawler class.

# creation of the filter more than 5 words function
# using a dataframe as a parameter.
def filter_more_five_words(dataframe):
    # declaration of a variable as a "menu".
    filter_menu = """"
    Please, enter the following option to filter
    the news titles with more than 5 words
    (ordered by the number of comments) \n
    2. Filter the titles 🟧: """
    # this while loop is to check if the user enter 
    # an incorrect value, the program can "ask" again.
    while True:
        # handle the entered option.
        # if the option is a word it displays an error.
        try:
            # declare an option entered in the program.
            filter_option = int(input(filter_menu))
            # if statement to handle incorrect values.
            if filter_option != 2:
                print("Please, enter a valid number.")
            else:
                # interactive messages.
                print("""
                Filtering the titles... 🔃\n
                """)
                try:
                    # invoke the "filter_more_five_words()" method from
                    # the crawler class, with a previous try except to 
                    # handle errors.
                    filtered_df = ycrawler.filter_more_five_words(dataframe)
                    print("Done! You can see the filtered titles in the following dataframe 👇🏻: \n")
                    # return the filtered datafram and brak the while loop.
                    return filtered_df
                    break
                except:
                    print("Sorry, it was an error, try again.")
        except ValueError:
            print("Please, enter a number.")


# creation of the filter less or equal than 5 words function
# using a dataframe as a parameter.
# this function is like the above function but with the 
# corresponding invocation of the "filter_less_five_words()" method.
def filter_less_five_words(dataframe):
    filter_menu = """"
    Please, enter the following option to filter
    the news titles with less or equal than 5 words
    (ordered by the number of points) \n
    3. Filter the titles 🟥: """
    while True:
        try:
            filter_option = int(input(filter_menu))
            if filter_option != 3:
                print("Please, enter a valid number.")
            else:
                print("""
                Filtering the titles... 🔃\n
                """)
                try:
                    filtered_df = ycrawler.filter_less_five_words(dataframe)
                    print("Done! You can see the filtered titles in the following dataframe 👇🏻: \n")
                    return filtered_df
                    break
                except:
                    print("Sorry, it was an error, try again.")
        except ValueError:
            print("Please, enter a number.")


# creation of the save data in an Excel file function
# with the three dataframes returned in the other functions.
# this function is like the above functions with a main difference.
def save_data_excel(og_df, fil_df1, fil_df2):
    save_menu = """
    This program can save the retrieve data in
    an Excel file 📂."""
    print(save_menu)
    while True:
        save_response = input("Do you want to save the data? 🤔 y/n: ")
        # if statement to handle incorrect values.
        if save_response != 'y' and save_response != 'n':
            print("Please, enter a correct value.")
        else:
            if save_response == 'y':
                # creation of an Excel file with Pandas, called 
                # "scraped_data.xlsx", then fill it with the dataframes
                # created previously.
                with pd.ExcelWriter("scraped_data.xlsx") as writer:
                    # with the "to_excel()" method you can save the dataframe
                    # in the Excel file (like a writer object), inside
                    # specific sheets.
                    og_df.to_excel(writer, sheet_name="Original_Data")
                    fil_df1.to_excel(writer, sheet_name="More_than_5_words")
                    fil_df2.to_excel(writer, sheet_name="Less_than_5_words")
                print("Done! You can check the Excel file called scraped_data.xlsx.")
                break
            else:
                break
    print("Thank you for use the YCombinator Hacker News Web Crawler! 🙂 by Daniel Erazo.")
    

# creation of the main() function.
# this function invokes the previous functions
# displaying different menus and messages and 
# handling the errors like the above functions.
def main():
    menu = """
    Welcome to the YCombinator Hacker News Web Crawler 🕷️
    Please, select the following option to retrieve the 
    first 30 entries on the page.\n
    1. Launch the crawler 🕸️: """    
    try:
        option = int(input(menu))
        if option != 1:
            print("Please, enter a valid number.")
        else:
            print("""
            Retrieving the order number, title, points and 
            comments from the entries on the site... 🔃\n
            """)
            try:
                entries_df = ycrawler.get_entries()
                print("Done! You can see the top 5 entries in the following dataframe 👇🏻: \n")
                print(entries_df.head(), "\n")
            except:
                print("Sorry, it was an error, try again.")

            while True:
                response = input(("Do you want to see the full dataframe? 🤔 y/n: "))
                if response != 'y' and response != 'n':
                    print("Please, enter a correct value.")
                else:
                    if response == 'y':
                        print(entries_df)
                        break
                    else:
                        break
            # these lines calls the previous functions and prints the dataframes.
            fil_df1 = filter_more_five_words(entries_df)
            print(fil_df1)
            fil_df2 = filter_less_five_words(entries_df)
            print(fil_df2)
            save_data_excel(entries_df, fil_df1, fil_df2)

    except ValueError:
        print("\tPlease, enter a number.")


# finally, creation of the entry point to invoke the main function.
if __name__ == '__main__':
    main()
