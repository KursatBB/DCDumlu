from prettytable import PrettyTable

def Helper():
    helpTable = PrettyTable(["Commands", "Descriptions"])
    helpTable.align = "l"
    helpTable.add_row(["getDomainInfo", "Get domain SID, name and MAQ"])
    helpTable.add_row(["sidToObject", "Convert SID to object name"])
    helpTable.add_row(["getPasswordPolicy", "Get password policy"])
    helpTable.add_row(["getPasswordNotRequired", "Get all users not required to have a password"])
    helpTable.add_row(["getTrustInfo", "Get trust relationship information"])
    helpTable.add_row(["getHosts","Dump hosts information"])
    helpTable.add_row(["getDCs","Get Domain Controller(s) information"])
    helpTable.add_row(["getUsers", "Dump users information"])
    helpTable.add_row(["getGroups", "Dump groups information"])
    helpTable.add_row(["hostDescriptions", "Dump description of hosts information"])
    helpTable.add_row(["userDescriptions", "Dump description of users information"])
    helpTable.add_row(["getGroupMembers", "Dump members of specified group"])
    helpTable.add_row(["searchUser", "Search specific user"])
    helpTable.add_row(["searchHost", "Search specific host"])
    helpTable.add_row(["unconstrainedComputer", "Enumerate unconstrained computer account"])
    helpTable.add_row(["constrainedComputer", "Enumerate constrained computer account"])
    helpTable.add_row(["constrainedUser", "Enumerate constrained user account"])
    helpTable.add_row(["unconstrainedUser", "Enumerate unconstrained user account"])
    helpTable.add_row(["getRbcd", "Enumerate resource-based constrained delegation configuration"])
    helpTable.add_row(["addUser", "Add a user"])
    helpTable.add_row(["addUserToGroup", "Add a user to group"])
    helpTable.add_row(["delUser", "Delete a user"])
    helpTable.add_row(["getSpns", "Getting all Kerberoastable users"])
    helpTable.add_row(["setSpn", "Set a servicePrincipalName attribute value"])
    helpTable.add_row(["unSetSpn", "Unset a servicePrincipalName attribute value"])
    helpTable.add_row(["addUnconstrained", "Modify an object for delegation to any service with Kerberos Auth."])
    helpTable.add_row(["addConstrained", "Modify an object for delegation to specific service"])
    helpTable.add_row(["getAsRep", "Getting all Asreproastable users"])
    helpTable.add_row(["addAsRepRoasting", "Set user option as do not require Kerberos preauthentication for As-Rep Roasting attack"])
    helpTable.add_row(["delAsRepRoasting", "Set user option as Kerberos preauthentication is required"])
    helpTable.add_row(["resetObject", "Change userAccountControl attribute of object to reset modifications that are Kerberos delegation attacks"])
    helpTable.add_row(["uacTable", "Show values for userAccountControl attribute if you need for resetObject operation"])
    helpTable.add_row(["checkConnection", "Get connection details"])
    helpTable.add_row(["help", "Print usage"])
    helpTable.add_row(["?", "Print usage"])
    helpTable.add_row(["exit", "Exit"])
    print(helpTable)

