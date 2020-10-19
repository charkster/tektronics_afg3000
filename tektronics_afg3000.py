import time

class tektronics_afg3000():

    def __init__(self, pyvisa_instr):
        self.tekafg3102 = pyvisa_instr

    def get_all_scpi_dict(self):
        channel_list = [1, 2]
        result_dict = {}
        for channel in channel_list:
            for command in self.output_w_channel_dict:
                time.sleep(0.1)
                result = (self.tekafg3102.query(command.format(channel, "?"))).rstrip('\r\n')
                result = " " + result
                result_dict[command.format(channel, "?")] = result
        for channel in channel_list:
            for command in self.source_w_channel_dict:
                time.sleep(0.1)
                result = (self.tekafg3102.query(command.format(channel, "?"))).rstrip('\r\n')
                result = " " + result
                result_dict[command.format(channel, "?")] = result
        for command in self.trigger_dict:
            result = (self.tekafg3102.query(command.format("?"))).rstrip('\r\n')
            result = " " + result
            result_dict[command.format("?")] = result
        return result_dict

    def get_all_scpi_list(self):
        channel_list = [1, 2]
        result_list = []
        for channel in channel_list:
            for command in self.output_w_channel_dict:
                time.sleep(0.1)
                result = (self.tekafg3102.query(command.format(channel, "?"))).rstrip('\r\n')
                result = " " + result
                result_list.append(command.format(channel, result))
        for channel in channel_list:
            for command in self.source_w_channel_dict:
                time.sleep(0.1)
                result = (self.tekafg3102.query(command.format(channel, "?"))).rstrip('\r\n')
                result = " " + result
                result_list.append(command.format(channel, result))
        for command in self.trigger_dict:
            result = (self.tekafg3102.query(command.format("?"))).rstrip('\r\n')
            result = " " + result
            result_list.append(command.format(result))
        return result_list

    def get_unique_scpi_list(self):
        unique_scpi_list = []
        inst_settings_list = self.get_all_scpi_list()
        for setting in inst_settings_list:
            if (setting not in self.settings_por_scpi_list):
                unique_scpi_list.append(setting)
        return unique_scpi_list

    output_w_channel_dict = {
        "OUTPut{0}:IMPedance{1}" : "Set/query impedance",
        "OUTPut{0}:POLarity{1}"  : "Set/query polarity",
        "OUTPut{0}:STATe{1}"     : "Set/query output 1 or 0"
        }

    output_dict = {
        "OUTPut:TRIGger:MODE{}" : "Set/query the mode of Trigger Output. mode=TRIGger,SYNC"
        }

    source_dict = {
        "SOURce:ROSCillator:SOURce{0}" : "Set/query clock reference input"
        }

    source_w_channel_dict = {
        "SOURce{0}:AM:STATe{1}"                          : "Set/query amplitude modulation status",
        "SOURce{0}:AM:INTernal:FREQuency{1}"             : "Set/query internal modulation frequency",
        "SOURce{0}:AM:INTernal:FUNCtion{1}"              : " Set/query modulation waveform setting",
        "SOURce{0}:AM:INTernal:FUNCtion:EFILe{1}"        : " Set/query EFILe setting",
        "SOURce{0}:AM:SOURce{1}"                         : " Set/query amplitude modulation source",
        "SOURce{0}:AM:DEPTh{1}"                          : " Set/query amplitude modulation depth",
        "SOURce{0}:BURSt:MODE{1}"                        : " Set/query burst mode",
        "SOURce{0}:BURSt:NCYCles{1}"                     : " Set/query burst mode waveform output cycle",
        "SOURce{0}:BURSt:TDELay{1}"                      : "Set/query burst mode trigger delay time",
        "SOURce{0}:BURSt:STATe{1}"                       : "Set/query burst mode status",
        "SOURce{0}:COMBine:FEED{1}"                      : "Set/query internal noise or external signal",
        "SOURce{0}:FM:INTernal:FREQuency{1}"             : "Set/query internal modulation frequency",
        "SOURce{0}:FM:INTernal:FUNCtion{1}"              : "Set/query internal modulation waveform",
        "SOURce{0}:FM:INTernal:FUNCtion:EFILe{1}"        : "Set/query EFILe setting",
        "SOURce{0}:FM:SOURce{1}"                         : "Set/query frequency modulation source",
        "SOURce{0}:FM:STATe{1}"                          : "Set/query frequency modulation status",
        "SOURce{0}:FM:DEViation{1}"                      : "Set/query frequency deviation",
        "SOURce{0}:FREQuency:CENTer{1}"                  : "Set/query center frequency",
        "SOURce{0}:FREQuency:CONCurrent:STATe{1}"        : "Set/query concurrent change of frequency",
        "SOURce{0}:FREQuency:MODE{1}"                    : "Set/query sweep status",
        "SOURce{0}:FREQuency:SPAN{1}"                    : "Set/query sweep frequency span",
        "SOURce{0}:FREQuency:STARt{1}"                   : "Set/query sweep start frequency",
        "SOURce{0}:FREQuency:STOP{1}"                    : " Set/query sweep stop frequency",
        "SOURce{0}:FREQuency:CW{1}"                      : "Set/query output waveform frequency, CW",
        "SOURce{0}:FREQuency:FIXed{1}"                   : "Set/query output waveform frequency, FIXed",
        "SOURce{0}:FSKey:INTernal:RATE{1}"               : "Set/query FSK internal modulation rate",
        "SOURce{0}:FSKey:SOURce{1}"                      : "Set/query FSK source",
        "SOURce{0}:FSKey:STATe{1}"                       : "Set/query FSK status",
        "SOURce{0}:FSKey:FREQuency{1}"                   : "Set/query FSK hop frequency",
        "SOURce{0}:FUNCtion:RAMP:SYMMetry{1}"            : "Set/query ramp waveform symmetry",
        "SOURce{0}:FUNCtion:SHAPe{1}"                    : "Set/query output waveform",
        "SOURce{0}:FUNCtion:EFILe{1}"                    : "Set/query EFILe name",
#        "SOURce{0}:PHASe:INITiate"                        : "Initiate output waveform phase synchronization",
        "SOURce{0}:PHASe:ADJust{1}"                      : "Set/query output waveform phase",
        "SOURce{0}:PM:INTernal:FREQuency{1}"             : "Set/query internal modulation frequency",
        "SOURce{0}:PM:INTernal:FUNCtion{1}"              : "Set/query internal modulation waveform",
        "SOURce{0}:PM:INTernal:FUNCtion:EFILe{1}"        : "Set/query EFILe name",
        "SOURce{0}:PM:SOURce{1}"                         : "Set/query phase modulation source",
        "SOURce{0}:PM:STATe{1}"                          : "Set/query phase modulation status",
        "SOURce{0}:PM:DEViation{1}"                      : "Set/query phase modulation deviation",
#        "SOURce{0}:POWer:LEVel:IMMediate:AMPLitude{1}"   : "Set/query internal noise level",
        "SOURce{0}:PULSe:DCYCle{1}"                      : "Set/query pulse waveform duty cycle",
        "SOURce{0}:PULSe:DELay{1}"                       : "Set/query pulse waveform lead delay",
        "SOURce{0}:PULSe:HOLD{1}"                        : "Set/query pulse waveform parameter",
        "SOURce{0}:PULSe:PERiod{1}"                      : "Set/query pulse waveform period",
        "SOURce{0}:PULSe:TRANsition:LEADing{1}"          : "Set/query pulse waveform leading edge time",
        "SOURce{0}:PULSe:TRANsition:TRAiling{1}"         : "Set/query pulse waveform trailing edge time",
        "SOURce{0}:PULSe:WIDTh{1}"                       : "Set/query pulse waveform width",
        "SOURce{0}:PWM:INTernal:FREQuency{1}"            : "Set/query pulse width modulation frequency",
        "SOURce{0}:PWM:INTernal:FUNCtion{1}"             : "Set/query pulse width modulation waveform",
        "SOURce{0}:PWM:INTernal:FUNCtion:EFILe{1}"       : "Set/query EFILe name",
        "SOURce{0}:PWM:SOURce{1}"                        : "Set/query pulse width modulation source",
        "SOURce{0}:PWM:STATe{1}"                         : "Set/query pulse width modulation status",
        "SOURce{0}:PWM:DEViation:DCYCle{1}"              : "Set/query pulse width modulation deviation",
        "SOURce{0}:SWEep:HTIMe{1}"                       : "Set/query sweep hold time",
        "SOURce{0}:SWEep:MODE{1}"                        : "Set/query sweep mode",
        "SOURce{0}:SWEep:RTIMe{1}"                       : "Set/query sweep return time",
        "SOURce{0}:SWEep:SPACing{1}"                     : "Set/query sweep spacing",
        "SOURce{0}:SWEep:TIME{1}"                        : "Set/query sweep time",
        "SOURce{0}:VOLTage:CONCurrent:STATe{1}"          : "Set/query concurrent change of amplitude level",
        "SOURce{0}:VOLTage:LIMit:HIGH{1}"                : "Set/query output amplitude upper limit",
        "SOURce{0}:VOLTage:LIMit:LOW{1}"                 : "Set/query output amplitude lower limit",
        "SOURce{0}:VOLTage:UNIT{1}"                      : "Set/query output amplitude units",
        "SOURce{0}:VOLTage:LEVel:IMMediate:HIGH{1}"      : "Set/query output amplitude high level",
        "SOURce{0}:VOLTage:LEVel:IMMediate:LOW{1}"       : "Set/query output amplitude low level",
        "SOURce{0}:VOLTage:LEVel:IMMediate:OFFSet{1}"    : "Set/query output offset voltage",
        "SOURce{0}:VOLTage:LEVel:IMMediate:AMPLitude{1}" : "Set/query output amplitude"
    }

    # these appear to not work on AFG3102
    trigger_dict = {
        "TRIGger:SEQuence:SLOPe{0}"  : "Set/query the slope of trigger signal",
        "TRIGger:SEQuence:SOURce{0}" : "Set/query the source of trigger signal",
        "TRIGger:SEQuence:TIMer{0}"  : "Set/query the period of internal clock"
    }

    trigger_cmd_dict = {
        "ABORt"                      : "Initialize trigger system",
        "*TRG"                       : "Force trigger event",
        "TRIGger:SEQuence:IMMediate" : "Generate a trigger event"
    }

    settings_por_scpi_list = [ 'OUTPut1:POLarity NORM',
                               'OUTPut1:IMPedance 50E0',
                               'OUTPut1:STATe 0',
                               'OUTPut2:POLarity NORM',
                               'OUTPut2:IMPedance 50E0',
                               'OUTPut2:STATe 0',
                               'SOURce1:AM:INTernal:FUNCtion SIN',
                               'SOURce1:AM:INTernal:FUNCtion:EFILe ""',
                               'SOURce1:PULSe:TRANsition:LEADing 5.00E-9',
                               'SOURce1:COMBine:FEED ""',
                               'SOURce1:PM:STATe 0',
                               'SOURce1:SWEep:HTIMe 0E-3',
                               'SOURce1:PULSe:DELay 0.00E-9',
                               'SOURce1:FREQuency:STARt 100.000000E3',
                               'SOURce1:FREQuency:STOP 1.00000000E6',
                               'SOURce1:FUNCtion:RAMP:SYMMetry 50.0',
                               'SOURce1:BURSt:MODE TRIG',
                               'SOURce1:VOLTage:LEVel:IMMediate:AMPLitude 1.000E0',
                               'SOURce1:VOLTage:LIMit:LOW -10.00E0',
                               'SOURce1:AM:STATe 0',
                               'SOURce1:BURSt:NCYCles 5E0',
                               'SOURce1:FREQuency:CW 1.00000000000E6',
                               'SOURce1:SWEep:MODE AUTO',
                               'SOURce1:PM:DEViation 1.57080',
                               'SOURce1:FREQuency:MODE CW',
                               'SOURce1:PM:SOURce INT',
                               'SOURce1:VOLTage:LIMit:HIGH 10.00E0',
                               'SOURce1:PULSe:HOLD DUTY',
                               'SOURce1:VOLTage:LEVel:IMMediate:LOW -500E-3',
                               'SOURce1:FM:SOURce INT',
                               'SOURce1:PWM:SOURce INT',
                               'SOURce1:PULSe:DCYCle 50.000',
                               'SOURce1:FM:STATe 0',
                               'SOURce1:PM:INTernal:FUNCtion SIN',
                               'SOURce1:VOLTage:LEVel:IMMediate:HIGH 500E-3',
                               'SOURce1:VOLTage:LEVel:IMMediate:OFFSet 0E-3',
                               'SOURce1:PWM:STATe 0',
                               'SOURce1:FREQuency:FIXed 1.00000000000E6',
                               'SOURce1:PM:INTernal:FREQuency 10.00E3',
                               'SOURce1:PULSe:PERiod 1.00000E-6',
                               'SOURce1:FREQuency:SPAN 900.000000E3',
                               'SOURce1:FUNCtion:EFILe ""',
                               'SOURce1:FSKey:INTernal:RATE 50.00E0',
                               'SOURce1:SWEep:RTIMe 1E-3',
                               'SOURce1:PULSe:WIDTh 500.00E-9',
                               'SOURce1:PM:INTernal:FUNCtion:EFILe ""',
                               'SOURce1:FM:DEViation 1.000000E6',
                               'SOURce1:BURSt:TDELay 0.0E-9',
                               'SOURce1:PWM:INTernal:FREQuency 10.00E3',
                               'SOURce1:PWM:DEViation:DCYCle 5.0',
                               'SOURce1:FM:INTernal:FUNCtion:EFILe ""',
                               'SOURce1:AM:DEPTh 50.0',
                               'SOURce1:VOLTage:CONCurrent:STATe 0',
                               'SOURce1:FM:INTernal:FREQuency 10.00E3',
                               'SOURce1:FREQuency:CONCurrent:STATe 0',
                               'SOURce1:SWEep:TIME 10E-3',
                               'SOURce1:PWM:INTernal:FUNCtion:EFILe ""',
                               'SOURce1:VOLTage:UNIT VPP',
                               'SOURce1:AM:SOURce INT',
                               'SOURce1:PWM:INTernal:FUNCtion SIN',
                               'SOURce1:SWEep:SPACing LIN',
                               'SOURce1:PULSe:TRANsition:TRAiling 5.00E-9',
                               'SOURce1:BURSt:STATe 0',
                               'SOURce1:FSKey:FREQuency 1.000000E6',
                               'SOURce1:FSKey:STATe 0',
                               'SOURce1:FM:INTernal:FUNCtion SIN',
                               'SOURce1:AM:INTernal:FREQuency 10.00E3',
                               'SOURce1:FUNCtion:SHAPe SIN',
                               'SOURce1:FSKey:SOURce INT',
                               'SOURce1:PHASe:ADJust 0.00000',
                               'SOURce1:FREQuency:CENTer 550.000000E3',
                               'SOURce2:AM:INTernal:FUNCtion SIN',
                               'SOURce2:AM:INTernal:FUNCtion:EFILe ""',
                               'SOURce2:PULSe:TRANsition:LEADing 5.00E-9',
                               'SOURce2:COMBine:FEED ""',
                               'SOURce2:PM:STATe 0',
                               'SOURce2:SWEep:HTIMe 0E-3',
                               'SOURce2:PULSe:DELay 0.00E-9',
                               'SOURce2:FREQuency:STARt 100.000000E3',
                               'SOURce2:FREQuency:STOP 1.00000000E6',
                               'SOURce2:FUNCtion:RAMP:SYMMetry 50.0',
                               'SOURce2:BURSt:MODE TRIG',
                               'SOURce2:VOLTage:LEVel:IMMediate:AMPLitude 1.000E0',
                               'SOURce2:VOLTage:LIMit:LOW -10.00E0',
                               'SOURce2:AM:STATe 0',
                               'SOURce2:BURSt:NCYCles 5E0',
                               'SOURce2:FREQuency:CW 1.00000000000E6',
                               'SOURce2:SWEep:MODE AUTO',
                               'SOURce2:PM:DEViation 1.57080',
                               'SOURce2:FREQuency:MODE CW',
                               'SOURce2:PM:SOURce INT',
                               'SOURce2:VOLTage:LIMit:HIGH 10.00E0',
                               'SOURce2:PULSe:HOLD DUTY',
                               'SOURce2:VOLTage:LEVel:IMMediate:LOW -500E-3',
                               'SOURce2:FM:SOURce INT',
                               'SOURce2:PWM:SOURce INT',
                               'SOURce2:PULSe:DCYCle 50.000',
                               'SOURce2:FM:STATe 0',
                               'SOURce2:PM:INTernal:FUNCtion SIN',
                               'SOURce2:VOLTage:LEVel:IMMediate:HIGH 500E-3',
                               'SOURce2:VOLTage:LEVel:IMMediate:OFFSet 0E-3',
                               'SOURce2:PWM:STATe 0',
                               'SOURce2:FREQuency:FIXed 1.00000000000E6',
                               'SOURce2:PM:INTernal:FREQuency 10.00E3',
                               'SOURce2:PULSe:PERiod 1.00000E-6',
                               'SOURce2:FREQuency:SPAN 900.000000E3',
                               'SOURce2:FUNCtion:EFILe ""',
                               'SOURce2:FSKey:INTernal:RATE 50.00E0',
                               'SOURce2:SWEep:RTIMe 1E-3',
                               'SOURce2:PULSe:WIDTh 500.00E-9',
                               'SOURce2:PM:INTernal:FUNCtion:EFILe ""',
                               'SOURce2:FM:DEViation 1.000000E6',
                               'SOURce2:BURSt:TDELay 0.0E-9',
                               'SOURce2:PWM:INTernal:FREQuency 10.00E3',
                               'SOURce2:PWM:DEViation:DCYCle 5.0',
                               'SOURce2:FM:INTernal:FUNCtion:EFILe ""',
                               'SOURce2:AM:DEPTh 50.0',
                               'SOURce2:VOLTage:CONCurrent:STATe 0',
                               'SOURce2:FM:INTernal:FREQuency 10.00E3',
                               'SOURce2:FREQuency:CONCurrent:STATe 0',
                               'SOURce2:SWEep:TIME 10E-3',
                               'SOURce2:PWM:INTernal:FUNCtion:EFILe ""',
                               'SOURce2:VOLTage:UNIT VPP',
                               'SOURce2:AM:SOURce INT',
                               'SOURce2:PWM:INTernal:FUNCtion SIN',
                               'SOURce2:SWEep:SPACing LIN',
                               'SOURce2:PULSe:TRANsition:TRAiling 5.00E-9',
                               'SOURce2:BURSt:STATe 0',
                               'SOURce2:FSKey:FREQuency 1.000000E6',
                               'SOURce2:FSKey:STATe 0',
                               'SOURce2:FM:INTernal:FUNCtion SIN',
                               'SOURce2:AM:INTernal:FREQuency 10.00E3',
                               'SOURce2:FUNCtion:SHAPe SIN',
                               'SOURce2:FSKey:SOURce INT',
                               'SOURce2:PHASe:ADJust 0.00000',
                               'SOURce2:FREQuency:CENTer 550.000000E3',
                               'TRIGger:SEQuence:SOURce TIM',
                               'TRIGger:SEQuence:SLOPe POS',
                               'TRIGger:SEQuence:TIMer 1.000E-3' ]

    settings_load_trans_list = [ 'SOURce1:PULSe:TRANsition:LEADing 1.000E-6',
                                 'SOURce1:VOLTage:LEVel:IMMediate:AMPLitude 2.000E0',
                                 'SOURce1:BURSt:NCYCles 1E0',
                                 'SOURce1:FREQuency:CW 1.000000E0',
                                 'SOURce1:PULSe:HOLD WIDT',
                                 'SOURce1:VOLTage:LEVel:IMMediate:LOW 0E-3',
                                 'SOURce1:PULSe:DCYCle 0.100',
                                 'SOURce1:VOLTage:LEVel:IMMediate:HIGH 2.000E0',
                                 'SOURce1:VOLTage:LEVel:IMMediate:OFFSet 1.000E0',
                                 'SOURce1:FREQuency:FIXed 1.000000E0',
                                 'SOURce1:PULSe:PERiod 1.000000000E0',
                                 'SOURce1:PULSe:WIDTh 1.0000E-3',
                                 'SOURce1:FM:DEViation 1.00E0',
                                 'SOURce1:PWM:DEViation:DCYCle 0.1',
                                 'SOURce1:PULSe:TRANsition:TRAiling 1.000E-6',
                                 'SOURce1:BURSt:STATe 1',
                                 'SOURce1:FUNCtion:SHAPe PULS',
                                 'OUTPut:TRIGger:MODE "TRIGger"'
                                 ]
