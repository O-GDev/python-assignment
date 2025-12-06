mainMenu = """
Choose a menu
1.  Phone book
2.  Messages
3.  Chat
4.  Call Register
5.  Tones
6.  Settings
7.  Call divert
8.  Games
9.  Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM Services
""" 
phoneBook = """
1.  Search
2.  Service Nos
3.  Add name
4.  Erase
5.  Edit
6.  Assign tone
7.  Send b'card
8.  Options
9.  Speed dials
10. Voice tags
"""
messages = """
1.  Write messages
2.  Inbox
3.  Outbox
4.  Picture messages
5.  Templates
6.  Smileys
7.  Message settings
8.  Info service
9.  Voice mailbox number
10. Service command editor  
"""
callRegister = """
1.  Missed calls
2.  Recieved Calls
3.  Dialed numbers
4.  Erase recent call lists
5.  Show call duration
6.  Show call costs
7.  Call cost setting
8.  Prepaid credit
"""
tones = """
1.  Ringing tone
2.  Ringing volume
3.  Incoming call alert
4.  Composer
5.  Message alert tone
6.  Keypad tones
7.  Warning and game tones
8.  Vibrating alert
9.  Screen saver
"""
settings = """
1.  Call settings
2.  Phone settings
3.  Security settings
4.  Restore factory settings
"""
clockMenu = """
1.  Alarm clock
2.  Clock settings
3.  Date setting
4.  Stopwatch
5.  Countdown timer
6.  Auto update of date and time
"""
phoneBookOption = """
Options
1.  Type of view
2.  Memory status
"""
messageSettingsOption = """
1.  Set 1
2.  Common
"""
setOneOption = """
1.  Message centre number
2.  Messages sent as
3.  Message validity
"""
commonSetting = """
1.  Delivery reports
2.  Reply via same centre
3.  Character support
"""
#//        String callRegisterOption = """
#//Call Register
#//1.  Missed calls
#//2.  Received calls
#//3.  Dialled numbers
#//4.  Erase recent call lists
#//5.  Show call duration
#//6.  Show call costs
#//7.  Call cost settings
#//8.  Prepaid credit
#//"""
showCallDurationOption = """
Show call duration
1.  Last call duration
2.  All calls’ duration
3.  Received calls’ duration
4.  Dialled calls’ duration
5.  Clear timers
"""
showCallCost = """
Show call cost
1.  Last call cost
2.  All calls’ cost
3.  Clear counters
"""
callCostSetting = """
Call cost settings
1.  Call cost limit
2.  Show costs in
"""
#//        String tonesMenu = """
#//1.  Ringing tone
#//2.  Ringing volume
#//3.  Incoming call alert
#//4.  Composer
#//5.  Message alert tone
#//6.  Keypad tones
#//7.  Warning and game tones
#//8.  Vibrating alert
#//9.  Screen saver
#//"""
callSettings = """
1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer 1
"""
phoneSettings = """
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Lights2
6. Confirm SIM service actions
"""

securitySettings = """
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Phone security
6. Change access codes
"""


menuLoop:
while (true):
    print(mainMenu)
    selected = int(input("Select menu options: "))
    match selected:
        case 1:
            phoneBookLoop:
            while (true){
            print(phoneBook)
            phoneBookSelected = int(input("Select menu options: "))
            match phoneBookSelected:
                case 1: print("Search...")
                case 2: print("Service Number...")
                case 3: print("Add Name...")
                case 4: print("Erase...")
                case 5: print("Edit...")
                case 6: print("Assign tone...")
                case 7: print("Send b'card...")
                case 8:
                   phoneBookSelectedLoop:
                   while(true):
                        print(phoneBookOption)
                        optionSelected = int(input("Select menu options: "))
                        match optionSelected:
                            case 1: print("Type of view...")
                            case 2: print("Memory Status...")
                            case 0: 
                                break phoneBookSelectedLoop
                            case _: print("Select a valid option")
                case 9: print("Speed dials...")
                case 10: print("Voice tags...")
                case 0:
                    break phoneBookLoopLoop
                case _: print("Select a valid option")
        case 2: 
            messageLoop:
            while(true):
            
            print(messages)
            print("Select menu options: ")
            optionSelected = int(input("Select menu options: "))
            match optionSelected:
                case 1: print("Send a message...")
                case 2: print("Inbox...")
                case 3: print("Outbox...")
                case 4: print("Pictue messages...")
                case 5: print("Templates...")
                case 6: print("Smileys...")
                case 7:
                    messageSettingsLoop:
                    while(true):
                    print(messageSettingsOption) 
                    print("Select menu options: ")
                    int settingOptionSelected = input.nextInt()
                    match (settingOptionSelected):
                    case 1: 
                        settingOptionSelectedLoop:
                        while(true){
                        print(showCallDurationOption)
                        print("Select menu options: ")
                        int messageSettingOptionSelected = input.nextInt()
                        match (messageSettingOptionSelected) {
                        case 1: print("Message center number")
                        case 2: print("Message sent as")
                        case 3: print("Message validity")
                        case 0:
                            break settingOptionSelectedLoop
                        case _: print("Select a valid option")
                    case 2: 
                        commonSettingLoop:
                        while (true):
                        print(commonSetting)
                        print("Select menu options: ")
                        commonSettingOptionSelected = int(input("Select menu options: "))
                        match (commonSettingOptionSelected:
                            case 1: print("Delivery Report")
                            case 2: print("Reply via same center")
                            case 3: print("Character support")
                            case 0: 
                                break commonSettingLoop
                            case _: print("Select a valid option")
                    case 0:
                        break messageSettingsLoop
                    case _: print("Select a valid option")
            case 8: print("Info service...")
            case 9: print("Voice mailbox number...")
            case 10: print("Service command editor...")
            case 0: 
                break messageLoop
            case _: print("Select a valid option")

            }
        }
            
        }
        case 3: print("Start chat")
        case 4:
            callRegisterLoop:
            while(true):
            print(callRegister)
            print("Select menu options: ")
            callRegisterOptionSelected = int(input("Select menu options: "))
            match (callRegisterOptionSelected) {
            case 1: print("Missed calls")
            case 2: print("Recieved calls")
            case 3: print("Dialled numbers")
            case 4: print("Erase recent call lists")
            case 5: {
               callDurationLoop:
               while(true){ 
                print(showCallDurationOption)
                print("Select menu options: ")
                callDurationOptionSelected = int(input("Select menu options: "))
                match (callDurationOptionSelected) {
                    case 1: print("Last call duration")
                    case 2: print("All calls' duration")
                    case 3: print("Receive calls' duration")
                    case 4: print("Dialed calls' duration")
                    case 5: print("Clear timers")
                    case 0: {
                        break callDurationLoop
                    }
                    case _: print("Select a valid option")
                        }
                }
              }

            case 6: {
                callCostLoop:
                while(true){
                print(showCallCost)
                print("Select menu options: ")
                callCostOptionSelected = int(input("Select menu options: "))
                match (callCostOptionSelected) {
                  case 1: print("Last call cost")
                  case 2: print("All call's cost")
                  case 3: print("Clear counters")
                  case 0:  
                        break callCostLoop
                  case _: print("Select a valid option")
            case 7: 
                callCostSettingLoop:
                while(true){
                print(callCostSetting)
                print("Select menu options: ")
                callCostSettingSelected = int(input("Select menu options: "))
                match (callCostSettingSelected) {
                  case 1: print("Call cost limit")
                  case 2: print("Show costs in")
                  case 0:  {
                        break callCostSettingLoop
                    }
                  case _: print("Select a valid option")
                    }
                }
              }
            case 8: print("Prepaid credit")
            case 0: {
                        break callRegisterLoop
                    }
            case _: print("Select a valid option")
            }
            }
        }
        case 5: {
            tonesLoop:
            while(true){
            print(tones)
            print("Select menu options: ")
            tonesSettingSelected = int(input("Select menu options: "))
            match (tonesSettingSelected) {
              case 1: print("Ringing tone")
              case 2: print("Ringing volume")
              case 3: print("Incoming call alert")
              case 4: print("Composer")
              case 5: print("Message alert tone")
              case 6: print("Keypad tones")
              case 7: print("Warning and game tones")
              case 8: print("Vibrating alert")
              case 9: print("Screen saver")
              case 0: {
                break tonesLoop
                }
              case _: print("Select a valid option")
                }
            }
        }
        case 6: {
            settingsLoop:
            while (true){
            print(settings)
            print("Select menu options: ")
            settingSelected = int(input("Select menu options: "))
            match (settingSelected) {
              case 1: {
                 callSettingsLoop:
                 while (true){
                  print(callSettings)
                  print("Select menu options: ")
                  callSettingSelected = int(input("Select menu options: "))
                  match (callSettingSelected) {
                    case 1: print("Automatic redial")
                    case 2: print("Speed dialling")
                    case 3: print("Call waiting options")
                    case 4: print("Own number sending")
                    case 5: print("Phone line in use")
                    case 6: print("Automatic answer")
                    case 0: {
                        break callSettingsLoop
                        }
                    case _: print("Select a valid option")
                    }
                }
                }
              case 2: {
                  phoneSettingsLoop:
                  while(true){
                  print(phoneSettings)
                  print("Select menu options: ")
                  phoneSettingSelected = int(input("Select menu options: "))
                  match (phoneSettingSelected) {
                    case 1: print("Language")
                    case 2: print("Cell info display")
                    case 3: print("Welcome note")
                    case 4: print("Network selection")
                    case 5: print("Lights")
                    case 6: print("Confirm SIM service actions")
                    case 0: {
                        break phoneSettingsLoop
                        }
                    case _: print("Select a valid option")
                    }}
                }
              case 3: {
                    securitySettingsLoop:
                    while(true){
                    print(securitySettings)
                    print("Select menu options: ")
                    securitySettingSelected = int(input("Select menu options: "))
                    match (securitySettingSelected) {
                        case 1: print("PIN code request")
                        case 2: print("Call barring service")
                        case 3: print("Fixed dialling")
                        case 4: print("Closed user group")
                        case 5: print("Phone security")
                        case 6: print("Change access codes")
                        case 0: {
                            break securitySettingsLoop
                            }
                        case _: print("Select a valid option")
                     }
                     }
                }
              case 4: print("Restore factory settings")
              case 0: {
                  break settingsLoop
                  }
              case _: print("Select a valid option")
                }
            }
            }
        case 7: print("Call divert")
        case 8: print("Games")
        case 9: print("Calculator")
        case 10: print("Reminders")
        case 11: {
                clockLoop:
                while(true){
            print(clockMenu)
            print("Select menu options: ")
                  phoneSettingSelected = int(input("Select menu options: "))
                  match (phoneSettingSelected) {
                    case 1: print("Alarm Clock")
                    case 2: print("Clock settings")
                    case 3: print("Date setting")
                    case 4: print("Stopwatch")
                    case 5: print("Countdown timer")
                    case 6: print("Auto update of date and time")
                    case 0: {
                        break clockLoop
                        }
                    case _: print("Select a valid option")
                    }
                }
            }
        case 12: print("Profiles")
        case 13: print("SIM services")
        case _: print("Select a valid option")
           
