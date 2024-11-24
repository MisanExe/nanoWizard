
import utility
import logging

class nanoWizard :
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        logging.info(" Initialized wizard")

    commandList = ['reserved', 'Adjust-Tab-Size', 'Set-To-Default', '']
    NANORC = '/etc/nanorc'
    #NANORC = 'nano-default.txt'
    NANORC_BACKUP = ''
    NANORC_ls = ''
    issued_command = ""
    

    def runCommand(self, command)->bool:
        command_var = command.split()

        id = self.__id_command(command_var[0])
        logging.info(f" Command ID : {id}")
        
        #run command here
        if id == 1 : # adjust tab command
            logging.info(f" Command : {self.commandList[id]}")

            #backup file
            if self.__read_backup() and len(self.NANORC_BACKUP) > 0:
                try :
                    if self.__adjustTab(command_var[1]):
                        return True
                except Exception as e:
                    logging.error(f" Please enter Tab size\nLike --> {self.commandList[id]} <tabsize>")
                    return False
                
        return False
            

    '''
        returns a command index
    '''
    def __id_command(self, command)->int:
        index = 0
        if command in self.commandList:
            for comms in self.commandList :
                if comms in command :
                    return index
                
                index += 1
        logging.error(" Entered command does not exist :\nExisting commands incude : ")
        for line in self.commandList :
            print(f"\t Command : {line}")
        return -1
    

    
    def __adjustTab(self, newSize)->bool:

        try :
            #attempt to open nanorc and read it's content
            with open(self.NANORC, 'r') as nanorc_file:
                self.NANORC_ls = nanorc_file.read().split('\n')
        except Exception as e:
            logging.error(f"adjustTab() error : {e}")


        if utility.replaceLine(self.NANORC_ls, 'set tabsize', 'set tabsize '+str(newSize)) :

            #replace 
            try :
                with open(self.NANORC, 'w') as nanorc_file:
                    for line in self.NANORC_ls :
                        nanorc_file.write(line+'\n')
                    logging.info(f" Successfully set nano tab size to : {newSize}")
                    return True
            except Exception as e :
                logging.error(f"adjustTab() error : {e}")
                if self.SetNanoRC_To_Default() :
                    logging.info(" Restored Nanorc file")
                return False
        else :
            logging.error('failed to write settings to adjust tab size')
            if self.SetNanoRC_To_Default() :
                logging.info(" Restored Nanorc file")
            return False


    def SetNanoRC_To_Default(self)->bool :
        #open nano file for writing 
        try : 
            with open(self.NANORC, 'w') as nanorc_file :
                for line in self.NANORC_BACKUP:
                    nanorc_file.write(line+'\n')
            return True
        except Exception as e:
            logging.error(f" {e}")
            return False
        
        

    def __read_backup(self)->bool:
        try :
            #read default file in
            with open(self.NANORC, 'r') as nanorc_backup:
                self.NANORC_BACKUP = nanorc_backup.read().split('\n')
            return True
            
        except Exception as e :
            logging.error(f" {e}")
            return False
