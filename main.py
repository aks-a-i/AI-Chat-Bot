from translation import helper_strings
from database import data


def on_numbercommand(chat):
    if "1" in chat:
        acc_no = input("Enter your acc no.:")
        available = False
        for dict in data.account_details:
            if dict["account_number"] == acc_no:
                for key, value in dict.items():
                    print(key, ':', value)
                print(helper_strings.tail_end)
                available = True
        if available == False:
            print("No details available for this acc no")


    elif "2" in chat:
        acc_no = input('enter your acc no.')
        available = False
        for dict in data.transaction_history:
            if dict["account_number"] == acc_no:
                for key, value in dict.items():
                    print(key, ':', value)
                print(helper_strings.tail_end)
                available = True
                break
        if available == False:
            print("No transaction history available for this acc no")

    elif "3" in chat:
        print(helper_strings.connect_customercare)

    else:
        print(helper_strings.header, helper_strings.tail_end)


#def on_greeting(chat):
    #for greeting in helper_strings.greeting_list:
        #if greeting in chat.lower():
            #print(helper_strings.greeting_reply)
            #break


def main():
    chat = input("\nChat here-")
    on_numbercommand(chat)


chat = input("Chat here-")
print(helper_strings.greeting_reply)
while True:
    main()
