# script_connector.py connects all mini projects into one
"""

ebay: mini project list




"""

"""

local db <---> physical medium <--> local db

built PC sales - ebay
built PC sales - local
crypto mining
pc building
    hardware renting
    runescape bot farm
        scripts
            rs_bot_api miniproject
            rs_bot_farm scripts (rs_bot_api profile + gsheet_api profile + sequencer profile)
                schedule_manager (list of schedules and info about them)
                cycle_manager (list of cycles and info about them)
                task_manager (list of tasks and info about them)
                vpn_manager (list of vpns and info about them)
                net_manage scripts (switch pc or vm network to different VPN)
                task_data (specifics of a task)
                data_collector (to collect and process data from a run execution)
                historical_archiver (to store run executions and retrieve past execution data)
                environment_deploy (prep OS first time use: set network+install RuneLite+RSScripts + set firewall, etc)
                environment_run scripts (to launch the VM+OS+RuneLite+RSScripts+rs_bot_farm scripts)
                rs_bot_farm_manager (summarized data of all PCs, live PC stats, VMs, accounts, active schedules, etc)
                
                
ebay bulk sales
scripts
    ebay_api miniproject
    gsheet_api miniproject
    api_sequencer miniproject
    ebay_inventory scripts (gsheet_api profile + ebay object profile + sequencer profile)
    
    pc inventory ebay scripts (PC inventory <--> ebay objects)
    pc built-to-order ebay scripts (PC built-to-order inventory <--> ebay objects)
    pc inventory to built-to-order migrator scripts (PC built-to-order inventory <--> built to order PC inventory)
    
    bittrex_api trading scripts (convert from google scripts to python)
    
    flask_ui project
        ebay item inventory
        pc item and builds inventory
        rs_bot_farm_manager (dashboard of all PCs, live PC stats, VMs, accounts, active schedules, etc)
    
    built PC sales - local - description generator

"""