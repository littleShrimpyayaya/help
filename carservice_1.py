#!/bin/python3
import os
import sys
import argparse
import json
import re

log_open = True
def local_print(info):
    if log_open:
        print('----- ----- ----- ----- ' + str(info) + ' ----- ----- ----- -----')
    else:
        return False

_current_path_ = os.getcwd()

def current_path():
    return _current_path_

part_declaration    = 1
part_implementation = 2
WHENCE_START   = 0
WHENCE_CURRENT = 1
WHENCE_END     = 2

class CarService:
    def _init_variables(self):
        self.code_module                                = 'SettingService'
        self.indent                                     = '    '
        self.crlf                                       = '\n'
        self.continus                                   = '\\'
        self.const                                      = 'const'
        self.void                                       = 'void'
        self.voidp                                      = 'void*'
        self.uint8                                      = 'uint8'
        self.uint16                                     = 'uint16'
        self.uint32                                     = 'uint32'
        self.sint8                                      = 'int8'
        self.sint16                                     = 'int16'
        self.sint32                                     = 'int32'
        self.uint8p                                     = 'uint8*'
        self.uint16p                                    = 'uint16*'
        self.uint32p                                    = 'uint32*'
        self.sint8p                                     = 'int8*'
        self.sint16p                                    = 'int16*'
        self.sint32p                                    = 'int32*'
        self.ff                                         = '0xff'
        self.ffff                                       = '0xffff'
        self.ffffff                                     = '0xffffff'
        self.ffffffff                                   = '0xffffffff'
        self.null                                       = 'NULL'
        self.rte_function_write_prefix                  = 'Rte_Write'
        self.rte_function_read_prefix                   = 'Rte_Read'
        self.unsigned                                   = 'unsigned'
        self.signed                                     = 'signed'
        self.local_inline                               = 'static'

        self.version_start           = '/* DO NOT CHANGE THIS COMMENT!           << Start of version logging area >>                DO NOT CHANGE THIS COMMENT!*/'
        self.version_end             = '/* DO NOT CHANGE THIS COMMENT!           << End   of version logging area >>                DO NOT CHANGE THIS COMMENT!*/'
        self.include_start_auto      = '/* DO NOT CHANGE THIS COMMENT!           << Auto Start of include  area >>        DO NOT CHANGE THIS COMMENT!*/'
        self.include_end_auto        = '/* DO NOT CHANGE THIS COMMENT!           << Auto End   of include  area >>        DO NOT CHANGE THIS COMMENT!*/'
        self.include_start           = '/* DO NOT CHANGE THIS COMMENT!           << Start of include  area >>        DO NOT CHANGE THIS COMMENT!*/'
        self.include_end             = '/* DO NOT CHANGE THIS COMMENT!           << End   of include  area >>        DO NOT CHANGE THIS COMMENT!*/'
        self.function_impl_start   = '/* DO NOT CHANGE THIS COMMENT!           << Start of function implementation >>             DO NOT CHANGE THIS COMMENT!*/'
        self.function_impl_end     = '/* DO NOT CHANGE THIS COMMENT!           << End   of function implementation >>             DO NOT CHANGE THIS COMMENT!*/'

        self.macro                                 = 'macro'
        self.function                              = 'function'
        self.struct                                = 'struct'
        self.enum                                  = 'enum'
        self.function_pointer_type                 = 'function_pointer_type'
        self.items                                 = []
        self.items_includes                        = {}
        self.manager_file_h                        = 'settingservice_manager_test.h'
        self.manager_file_c                        = 'settingservice_manager_test.c'
        self.types_file_h                          = 'settingservice_types_test.h'
        self.macros_file_h                         = 'settingservice_macros_test.h'
        self.enums_file_h                          = 'settingservice_enumeration_test.h'
        self.enums_file_h                          = 'settingservice_enumeration_test.h'
        self.common_file_h                         = 'settingservice_common_api.h'
        self.common_file_c                         = 'settingservice_common_api.c'

    def _init_macros(self):
        self.items.append({ 'category': self.macro,     'name': 'constants_value', 'value': None,
            'implementation': None,
            'declaration': self._define_constants(),
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'INVALID_INIT_VALUE', 'value': self.ffffffff,
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'INVALID_DEFALUT_VALUE', 'value': self.ffffffff,
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'INVALID_FACTORY_VALUE', 'value': self.ffffffff,
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'PREVIOUS_VALUE_SIZE_0', 'value': 'U0',
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'PREVIOUS_VALUE_NULL', 'value': self.null,
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'INVALID_NVM_INDEX', 'value': self.ffffffff,
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'INVALID_NVM_INDEX_LENGTH', 'value': 'U0',
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'RTE_E_NVM_BLOCK_ID_74', 'value': 'U0',
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'RTE_E_NVM_BLOCK_ID_74_LENGTH', 'value': 'U32',
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'LOG_IMPL_USE_MACRO_SWITCH', 'value': '!!(U1)',
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'LOG_IMPL_USE_FUNCTION_SWITCH', 'value': '!(LOG_IMPL_USE_MACRO_SWITCH)',
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })
        self.items.append({ 'category': self.macro,     'name': 'LOG_IMPL_METHOD', 'value': '(LOG_IMPL_USE_MACRO_SWITCH)',
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.macros_file_h,
            'implementation_file': None,
            })

    def _init_functions(self):
        self.items.append({ 'category': self.function,  'name': 'init', 'prefix': None, 'suffix': None, 'return_type': self.uint8, 'arguments': [
            { 'name': None, 'type': None, 'description': None, },
            { 'name': 'msg', 'type': self.uint8, 'description': 'This is for message', },
            { 'name': None, 'type': None, 'description': None, },
            { 'name': 'data_len', 'type': self.uint16, 'description': None, },
            ],
            'implementation': self._init_function_implementation(),
            'declaration': None,
            'scope': None,
            'description': 'Initialize Function',
            'declaration_file': self.manager_file_h,
            'implementation_file': self.manager_file_c, 
            })
        self.items.append({ 'category': self.function,  'name': 'Local_Reset_Factory', 'prefix': None, 'suffix': None, 'return_type': self.void, 'arguments': [
            { 'name': None, 'type': None, 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': self.local_inline,
            'description': 'Local reset factory function',
            'declaration_file': self.manager_file_h,
            'implementation_file': self.manager_file_c, 
            })

    def _init_function_pointers(self):
        self.items.append({ 'category': self.function_pointer_type,  'name': 'Com_SR_CallBack_T', 'prefix': None, 'suffix': None, 'return_type': 'FUNC(void, COM_APPL_CODE)', 'arguments': [
            { 'name': None, 'type': None, 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': 'This is callback of rte sending successs.',
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.function_pointer_type,  'name': 'SettingServiceFunction_T', 'prefix': None, 'suffix': None, 'return_type': self.uint8, 'arguments': [
            { 'name': None, 'type': self.voidp, 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.function_pointer_type,  'name': 'SettingServiceCommonFunction_T', 'prefix': None, 'suffix': None, 'return_type': self.uint8, 'arguments': [
            { 'name': None, 'type': None, 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.function_pointer_type,  'name': 'SettingServiceStartupFunction_T', 'prefix': None, 'suffix': None, 'return_type': self.void, 'arguments': [
            { 'name': None, 'type': 'Startup_Method_T', 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.function_pointer_type,  'name': 'SettingServiceResetFunction_T', 'prefix': None, 'suffix': None, 'return_type': self.void, 'arguments': [
            { 'name': None, 'type': 'Reset_Method_T', 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.function_pointer_type,  'name': 'SettingServiceReceiveFunction_T', 'prefix': None, 'suffix': None, 'return_type': 'Result_T', 'arguments': [
            { 'name': None, 'type': 'Message_T*', 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.function_pointer_type,  'name': 'SettingServiceRunnableFunction_T', 'prefix': None, 'suffix': None, 'return_type': self.void, 'arguments': [
            { 'name': None, 'type': self.void, 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })

    def _init_structs(self):
        self.items.append({ 'category': self.struct,    'name': 'Message_T', 'prefix': None, 'suffix': None, 'members': [
            { 'name': None, 'type': None, 'description': None, },
            { 'name': 'msg_id', 'type': self.uint32, 'description': None, },
            { 'name': 'area_id', 'type': self.uint32, 'description': None, },
            { 'name': 'data', 'type': self.uint8p, 'description': None, },
            { 'name': 'data_len', 'type': self.uint16, 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': 'Struct of Message_T',
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.struct,    'name': 'SettingServiceInfo_T', 'prefix': None, 'suffix': None, 'members': [
            { 'name': 'signal_id', 'type': self.uint32, 'description': None, },
            { 'name': 'log_level', 'type': 'Log_Level_T', 'description': None, },
            { 'name': 'send_callback', 'type': 'Com_SR_CallBack_T', 'description': None, },
            { 'name': None, 'type': None, 'description': 'Start Of Defalut Variables Decalre', },
            { 'name': 'update_type', 'type': 'SettingServiceUpdate_T', 'description': None, },
            { 'name': 'direction', 'type': f'{self.const} SettingServiceDirection_T', 'description': None, },
            { 'name': 'sent_times', 'type': 'Send_Time_T', 'description': None, },
            { 'name': 'invoked_type', 'type': 'Function_Invoked_T', 'description': None, },
            { 'name': 'area_id', 'type': self.uint32, 'description': None, },
            { 'name': 'status', 'type': 'Sending_Status_T', 'description': None, },
            { 'name': None, 'type': None, 'description': 'End   Of Defalut Variables Decalre', },
            { 'name': None, 'type': None, 'description': 'Start of Manual Initailizing Variables Decalre', },
            { 'name': 'tx_hisip_id', 'type': self.uint32, 'description': None, },
            { 'name': 'rx_hisip_id', 'type': self.uint32, 'description': None, },
            { 'name': 'need_send_times', 'type': f'{self.const} Send_Time_T', 'description': None, },
            { 'name': 'end_value', 'type': f'{self.const} End_Value_T', 'description': None, },
            { 'name': 'init_value', 'type': f'{self.const} {self.uint32}', 'description': None, },
            { 'name': 'default_value', 'type': f'{self.const} {self.uint32}', 'description': None, },
            { 'name': 'factory_value', 'type': f'{self.const} {self.uint32}', 'description': None, },
            { 'name': 'nvm_index', 'type': f'{self.const} {self.uint32}', 'description': None, },
            { 'name': 'nvm_index_data_len', 'type': f'{self.const} {self.uint32}', 'description': None, },
            { 'name': 'pre_value_buffer', 'type': f'{self.uint8p}', 'description': None, },
            { 'name': 'pre_value_buffer_len', 'type': f'{self.uint16}', 'description': None, },
            { 'name': 'buffer', 'type': f'{self.uint8p}', 'description': None, },
            { 'name': 'buffer_len', 'type': f'{self.uint16}', 'description': None, },
            { 'name': None, 'type': None, 'description': 'You can add more new variables to use here.', },
            { 'name': None, 'type': None, 'description': 'End   of Manual Initailizing Variables Decalre.', },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.struct,    'name': 'SettingServiceObject_T', 'prefix': None, 'suffix': None, 'members': [
            { 'name': 'data', 'type': 'SettingServiceInfo_T', 'description': None, },
            { 'name': 'funcs', 'type': 'SettingServiceFunction_T*', 'description': None, },
            { 'name': 'funcs_size', 'type': self.uint8, 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.struct,    'name': 'Message_Queue_T', 'prefix': None, 'suffix': None, 'members': [
            { 'name': 'inIndex', 'type': self.uint32, 'description': None, },
            { 'name': 'outIndex', 'type': self.uint32, 'description': None, },
            { 'name': 'current_size', 'type': self.uint32, 'description': None, },
            { 'name': 'queue', 'type': 'SettingServiceObject_T**', 'description': None, },
            { 'name': 'max_size', 'type': self.uint32, 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })
        self.items.append({ 'category': self.struct,    'name': 'SettingServiceComponent_T', 'prefix': None, 'suffix': None, 'members': [
            { 'name': 'init', 'type': 'SettingServiceCommonFunction_T', 'description': None, },
            { 'name': 'finalize', 'type': 'SettingServiceCommonFunction_T', 'description': None, },
            { 'name': 'receive_message', 'type': 'SettingServiceReceiveFunction_T', 'description': None, },
            { 'name': 'android_starup', 'type': 'SettingServiceStartupFunction_T', 'description': None, },
            { 'name': 'reset', 'type': 'SettingServiceResetFunction_T', 'description': None, },
            { 'name': 'runnable_5ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            { 'name': 'runnable_10ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            { 'name': 'runnable_20ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            { 'name': 'runnable_40ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            { 'name': 'runnable_50ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            { 'name': 'runnable_80ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            { 'name': 'runnable_100ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            { 'name': 'runnable_160ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            { 'name': 'runnable_200ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            { 'name': 'runnable_320ms', 'type': 'SettingServiceRunnableFunction_T', 'description': None, },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': None,
            'declaration_file': self.types_file_h,
            'implementation_file': None, 
            })

    def _init_enums(self):
        self.items.append({ 'category': self.enum,      'name': 'Result_T', 'prefix': None, 'suffix': None, 'members': [
            { 'name': 'RES_OK', 'type': None, 'description': None, 'value': None },
            { 'name': 'RES_NOT_OK', 'type': None, 'description': None, 'value': None },
            { 'name': None, 'type': None, 'description': 'middle', },
            { 'name': 'RES_INVALID', 'type': None, 'description': None, 'value': None },
            { 'name': 'RESULT_T_END', 'type': None, 'description': None, 'value': self.ffffffff },
            { 'name': None, 'type': None, 'description': 'END', },
            ],
            'implementation': None,
            'declaration': None,
            'scope': None,
            'description': 'Enum of Result_T',
            'declaration_file': self.enums_file_h,
            'implementation_file': None, 
            })

    def _init_includes(self):
        self.items_includes[self.types_file_h] = {
                'system_includes': [
                    'stdio.h',
                    'stdlib.h',
                    ],
                'includes': [
                    'Rte_Type.h',
                    'dbg_tracer.h',
                    'hisip_msg_vip.h',
                    'settingservice_enumeration.h',
                    'settingservice_macros.h',
                    'Rte_CpAp_SettingService_Navigator.h',
                    'Appl_Cbk.h',
                    ],
                }

    def _get_includes_by_filename(self, filename):
        includes_string = None
        if filename:
            includes_item = self._get_item_value_by_key(filename, self.items_includes)
            if includes_item:
                includes_item_sys_incs = self._get_item_value_by_key('system_includes', includes_item)
                includes_item_incs     = self._get_item_value_by_key('includes', includes_item)
                for sys_inc in includes_item_sys_incs:
                    if includes_string:
                        includes_string += f'#include <{sys_inc}>{self.crlf}'
                    else:
                        includes_string  = f'#include <{sys_inc}>{self.crlf}'
                for inc in includes_item_incs:
                    if includes_string:
                        includes_string += f'#include "{inc}"{self.crlf}'
                    else:                                    
                        includes_string  = f'#include "{inc}"{self.crlf}'

        return includes_string

    def _init_items(self):
        self._init_includes()
        self._init_macros()
        self._init_functions()
        self._init_function_pointers()
        self._init_structs()
        self._init_enums()

    def __init__(self):
        self._init_variables()
        self._init_items()

    def _set_var(self, name, value):
        name = name.lower()
        setattr(self, name, value)

    def _get_var(self, name):
        name = name.lower()
        return getattr(self, name, None)

    def _get_item_value_by_key(self, key, item):
        value = None
        if item and key in item:
            value = item[key]

        return value

    def _define_constants(self):
        declaration = """#define    U0    (0u)
#define    U1    (1u)
#define    U2    (2u)
#define    U3    (3u)
#define    U4    (4u)
#define    U5    (5u)
#define    U6    (6u)
#define    U7    (7u)
#define    U8    (8u)
#define    U9    (9u)
#define    U10    (10u)
#define    U32    (32u)
        """

        return declaration

    def _macro_define(self, name, value):
        local_print(sys._getframe().f_code.co_name)
        expression = None
        if name and value:
            expression = '#define ' + name + f' ({value})'
        elif name:
            expression = '#define ' + name
        elif value:
            expression = '#define ' + value
        else:
            local_print(sys._getframe().f_code.co_name + ' None')

        return expression

    def _process_macros(self, item):
        local_print(sys._getframe().f_code.co_name)
        item_name          = self._get_item_value_by_key('name',  item)
        item_value         = self._get_item_value_by_key('value', item)
        item_description   = self._get_item_value_by_key('description', item)
        item_declaration  = self._get_item_value_by_key('declaration', item)
        if item_declaration == None:
            item_declaration   = self._macro_define(item_name, item_value)
        else:
            local_print(item_declaration)
        if item_description:
            item_declaration += '/* ' + item_description + ' */'
        if item_declaration:
            item_declaration += self.crlf
            item['declaration'] = item_declaration

    def _get_all_args_list_arguments(self, item):
        args = []
        arguments = self._get_item_value_by_key('arguments', item)
        if arguments:
            for arg_item in arguments:
                arg_name = self._get_item_value_by_key('name', arg_item)
                arg_type = self._get_item_value_by_key('type', arg_item)
                arg_desc = self._get_item_value_by_key('description', arg_item)
                if arg_name and arg_type:
                    if arg_desc:
                        args.append(f'{arg_type} {arg_name}/*{arg_desc}*/')
                    else:
                        args.append(f'{arg_type} {arg_name}')
                elif arg_type:
                    if arg_desc:
                        args.append(f'{arg_type} /*{arg_desc}*/')
                    else:
                        args.append(f'{arg_type}')
                elif arg_desc:
                    args.append(f'/*{arg_desc}*/')

        return args

    def _reconcat_string_with_list(self, arguments_list, deli):
        arguments_string = None
        is_comments_last_state = False
        if len(arguments_list) > 0:
            for arg in arguments_list:
                if arg.strip().startswith('/*') or arg.strip().startswith('//'):
                    if arguments_string:
                        arguments_string += arg
                    else:
                        arguments_string  = arg
                    is_comments_last_state = True
                else:
                    if arguments_string:
                        if is_comments_last_state == False:
                            arguments_string += arg
                        else:
                            arguments_string += deli + arg
                    else:
                        arguments_string  = arg
                    is_comments_last_state = False
                    
        return arguments_string

    def _get_arguments_string(self, item):
        arguments_string = None
        arguments_list = self._get_all_args_list_arguments(item)
        if len(arguments_list) > 0:
            arguments_string = ','.join(arguments_list)
            #arguments_string = self._reconcat_string_with_list(arguments_list, ',')
        return arguments_string

    def _function_validated_with_arguments(self, return_type, name, args):
        if return_type and name and args and len(args.strip()) > 0:
            return True
        return False

    def _function_validated_without_arguments(self, return_type, name, args):
        if return_type and name and args and len(args.strip()) > 0:
            return False
        elif return_type and name:
            return True
        return False

    def _function_declare_string(self, return_type, name, args, item):
        local_print(sys._getframe().f_code.co_name)
        declaration = None
        item_scope      = self._get_item_value_by_key('scope', item)
        if self._function_validated_with_arguments(return_type, name, args):
            if item_scope and item_scope.strip() == self.local_inline.strip():
                declaration = f'{self.local_inline} {return_type} {name}({args})'
            else:
                declaration = f'{return_type} {name}({args})'
        elif self._function_validated_without_arguments(return_type, name, args): 
            if item_scope and item_scope.strip() == self.local_inline.strip():
                declaration = f'{self.local_inline} {return_type} {name}({self.void})'
            else:
                declaration = f'{return_type} {name}({self.void})'
        return declaration

    def _function_declare(self, return_type, name, args, item):
        declaration = self._function_declare_string(return_type, name, args, item)
        if declaration:
            declaration += ';' + self.crlf
        return declaration

    def _init_function_implementation(self):
        function_string = None
        function_string = f"""{self.crlf}{self.indent}{self.uint8} ret = 0u;
{self.indent}ret = 1u;
{self.function_impl_start}

{self.function_impl_end}
{self.indent}return ret;
"""

        return function_string

    def _function_implementation_string(self, return_type, name, args, item):
        local_print(sys._getframe().f_code.co_name)
        implementation = None
        declaration = self._function_declare_string(return_type, name, args, item)
        item_implementation  = self._get_item_value_by_key('implementation', item)
        if declaration:
            implementation = f'{declaration}'
            implementation += self.crlf + '{'
            if self._function_validated_with_arguments(return_type, name, args):
                if item_implementation:
                    implementation += item_implementation
                else:
                    implementation += f'{self.crlf}{self.indent}{return_type} ret = 0u;'
                    implementation += self.crlf
                    implementation += f'{self.crlf}{self.indent}return ret;{self.crlf}'
            elif self._function_validated_without_arguments(return_type, name, args):
                if item_implementation:
                    implementation += item_implementation
                else:
                    implementation += self.crlf
            else:
                return None
            implementation += '}' + self.crlf
        return implementation

    def _function_implementation(self, return_type, name, args, item):
        implementation = self._function_implementation_string(return_type, name, args, item)
        if implementation:
            implementation += self.crlf
        return implementation

    def _function_pointers_declare_string(self, return_type, name, args, item):
        local_print(sys._getframe().f_code.co_name)
        declaration = None
        item_scope      = self._get_item_value_by_key('scope', item)
        if self._function_validated_with_arguments(return_type, name, args):
            declaration = f'typedef {return_type} (*{name})({args})'
        elif self._function_validated_without_arguments(return_type, name, args): 
            declaration = f'typedef {return_type} (*{name})({self.void})'
        return declaration

    def _function_pointers_declare(self, return_type, name, args, item):
        declaration = self._function_pointers_declare_string(return_type, name, args, item)
        if declaration:
            declaration += ';' + self.crlf
        return declaration

    def _function_pointers_implementation_string(self, return_type, name, args, item):
        local_print(sys._getframe().f_code.co_name)
        implementation = None
        declaration = self._function_declare_string(return_type, name, args, item)
        item_implementation  = self._get_item_value_by_key('implementation', item)
        if declaration:
            implementation = f'{declaration}'
            implementation += self.crlf + '{'
            if self._function_validated_with_arguments(return_type, name, args):
                if item_implementation:
                    implementation += item_implementation
                else:
                    implementation += f'{self.crlf}{self.indent}{return_type} ret = 0u;'
                    implementation += self.crlf
                    implementation += f'{self.crlf}{self.indent}return ret;{self.crlf}'
            elif self._function_validated_without_arguments(return_type, name, args):
                if item_implementation:
                    implementation += item_implementation
                else:
                    implementation += self.crlf
            else:
                return None
            implementation += '}' + self.crlf
        implementation = None
        return implementation

    def _function_pointers_implementation(self, return_type, name, args, item):
        implementation = self._function_pointers_implementation_string(return_type, name, args, item)
        if implementation:
            implementation += self.crlf
        return implementation

    def _process_functions(self, item):
        local_print(sys._getframe().f_code.co_name)
        function_return_type      = self._get_item_value_by_key('return_type', item)
        function_name             = self._get_item_value_by_key('name', item)
        function_arguments_string = self._get_arguments_string(item)

        item_declaration    = self._function_declare(function_return_type, function_name, function_arguments_string, item)
        item_implementation = self._function_implementation(function_return_type, function_name, function_arguments_string, item)
        item_description    = self._get_item_value_by_key('description', item)
        if item_declaration:
            if item_description:
                item['declaration'] = f'/* {item_description} */{self.crlf}{item_declaration}'
            else:
                item['declaration'] = f'{item_declaration}'
        if item_implementation:
            if item_description:
                item['implementation'] = f'/* {item_description} */{self.crlf}{item_implementation}'
            else:
                item['implementation'] = f'{item_implementation}'

    def _process_function_pointers(self, item):
        local_print(sys._getframe().f_code.co_name)
        function_return_type      = self._get_item_value_by_key('return_type', item)
        function_name             = self._get_item_value_by_key('name', item)
        function_arguments_string = self._get_arguments_string(item)

        item_declaration    = self._function_pointers_declare(function_return_type, function_name, function_arguments_string, item)
        item_implementation = self._function_pointers_implementation(function_return_type, function_name, function_arguments_string, item)
        item_description    = self._get_item_value_by_key('description', item)
        if item_declaration:
            if item_description:
                item['declaration'] = f'/* {item_description} */{self.crlf}{item_declaration}'
            else:
                item['declaration'] = f'{item_declaration}'
        if item_implementation:
            if item_description:
                item['implementation'] = f'/* {item_description} */{self.crlf}{item_implementation}'
            else:
                item['implementation'] = f'{item_implementation}'

    def _struct_declare(self, name, members):
        struct_declare = None
        if name:
            struct_declare = 'typedef struct {' + self.crlf
            if members:
                members = members.replace(',', f';') + self.crlf
                struct_declare += members
            struct_declare += '} ' + name + ';' + self.crlf

        return struct_declare

    def _get_all_args_list_members(self, item):
        args = []
        members = self._get_item_value_by_key('members', item)
        if members:
            for arg_item in members:
                arg_name = self._get_item_value_by_key('name', arg_item)
                arg_type = self._get_item_value_by_key('type', arg_item)
                arg_desc = self._get_item_value_by_key('description', arg_item)
                if arg_name and arg_type:
                    if arg_desc:
                        args.append(f'{self.indent}{arg_type} {arg_name}/* {arg_desc} */')
                    else:
                        args.append(f'{self.indent}{arg_type} {arg_name}')
                elif arg_type:
                    if arg_desc:
                       args.append(f'{self.indent}{arg_type} /* {arg_desc} */')
                    else:
                        args.append(f'{self.indent}{arg_type}')
                elif arg_desc:
                    args.append(f'{self.indent}/* {arg_desc} */')

        return args

    def _get_members_string_of_struct(self, item):
        members_list = self._get_all_args_list_members(item)
        members_string = self._concat_list_with_delimiter(members_list, f',', self.struct)
        return members_string

    def _process_structs(self, item):
        local_print(sys._getframe().f_code.co_name)
        item_name           = self._get_item_value_by_key('name', item)
        item_arguments      = self._get_members_string_of_struct(item)
        item_description    = self._get_item_value_by_key('description', item)
        item_declaration    = self._struct_declare(item_name, item_arguments)
        if item_declaration:
            if item_description:
                item['declaration'] = f'/* {item_description} */{self.crlf}{item_declaration}'
            else:
                item['declaration'] = f'{item_declaration}'
            
    def _get_all_args_list_members_enum(self, item):
        args = []
        members = self._get_item_value_by_key('members', item)
        if members:
            for member in members:
                name  = self._get_item_value_by_key('name', member)
                value = self._get_item_value_by_key('value', member)
                description = self._get_item_value_by_key('description', member)
                if name and value:
                    if description:
                        args.append(f'{self.indent}{name} = {value}/* {description} */')
                    else:
                        args.append(f'{self.indent}{name} = {value}')
                elif name:
                    if description:
                        args.append(f'{self.indent}{name}/* {description} */')
                    else:
                        args.append(f'{self.indent}{name}')
                elif description:
                        args.append(f'{self.indent}/* {description} */')
        return args

    def _is_comments(self, string):
        if string and string.strip().startswith('/*') or string.strip().startswith('//'):
            return True
        else:
            return False

    def _has_validated_data_next(self, fromI, members_list):
        has = False
        for i in range(fromI, len(members_list)):
            member = members_list[i]
            if self._is_comments(member):
                continue
            else:
                has = True
                break

        return has

    def _concat_list_with_delimiter_for_struct(self, members_list, delimiter):
        members_string = None
        last_state_is_comment = False
        if members_list:
            for i in range(len(members_list)):
                member = members_list[i]
                if i == 0:
                    members_string = member
                    if self._has_validated_data_next(i+1, members_list):
                        members_string += ','
                else:
                    members_string += member
                    if self._is_comments(member) == False:
                        members_string += ','
                members_string += self.crlf
        return members_string

    def _concat_list_with_delimiter_for_enum(self, members_list, delimiter):
        members_string = None
        last_state_is_comment = False
        if members_list:
            for i in range(len(members_list)):
                member = members_list[i]
                if i == 0:
                    members_string = member
                    if self._has_validated_data_next(i+1, members_list):
                        members_string += ','
                else:
                    members_string += member
                    if self._has_validated_data_next(i+1, members_list) and self._is_comments(member) == False:
                        members_string += ','
                members_string += self.crlf
        return members_string

    def _concat_list_with_delimiter(self, members_list, delimiter, category):
        members_string = None
        if category == self.enum:
            members_string = self._concat_list_with_delimiter_for_enum(members_list, delimiter)
        elif category == self.struct:
            members_string = self._concat_list_with_delimiter_for_struct(members_list, delimiter)

        return members_string

    def _get_members_string_of_enum(self, item):
        members_list = self._get_all_args_list_members_enum(item)
        members_string = self._concat_list_with_delimiter(members_list, f',', self.enum)
        return members_string

    def _enum_declare(self, name, members):
        enum_declare = None
        if name:
            if members:
                enum_declare = 'typedef enum {' + self.crlf + f'{members}' + self.crlf + '}' + f' {name};{self.crlf}'
            else:
                enum_declare = 'typedef enum {' + self.crlf + '}' + f' {name};{self.crlf}'

        return enum_declare

    def _process_enums(self, item):
        local_print(sys._getframe().f_code.co_name)
        item_declaration    = None
        item_members_string = None
        item_name           = self._get_item_value_by_key('name', item)
        item_members        = self._get_members_string_of_enum(item)
        item_declaration    = self._enum_declare(item_name, item_members)
        item_description    = self._get_item_value_by_key('description', item)
        if item_declaration:
            if item_description:
                item['declaration'] = f'/* {item_description} */{self.crlf}{item_declaration}'
            else:
                item['declaration'] = item_declaration
            
    def _process_items(self):
        local_print(sys._getframe().f_code.co_name)
        for item in self.items:
            if item and len(item) > 0:
                category = item['category']
                if category == self.macro:
                    self._process_macros(item)
                    local_print(item)
                elif category == self.function:
                    self._process_functions(item)
                    local_print(item)
                elif category == self.function_pointer_type:
                    self._process_function_pointers(item)
                    local_print(item)
                elif category == self.struct:
                    self._process_structs(item)
                    local_print(item)
                elif category == self.enum:
                    self._process_enums(item)
                    local_print(item)

    def _set_item_value_by_key(self, item, key, value):
        local_print(sys._getframe().f_code.co_name)
        if item:
            if key in item:
                item[key] = value

    def _item_found(self, item, name):
        local_print(sys._getframe().f_code.co_name)
        item_name = self._get_item_value_by_key('name', item)
        local_print(sys._getframe().f_code.co_name + f' item_name = {item_name}, name = {name}')
        if item_name and name:
            if item_name == name:
                local_print('Found: ' + name)
                return True

        return False

    def _update_item_by_config(self, config):
        local_print(sys._getframe().f_code.co_name)
        if config:
            name                 = self._get_item_value_by_key('name', config)
            declaration_file     = self._get_item_value_by_key('declaration_file', config)
            implementation_file  = self._get_item_value_by_key('implementation_file', config)
            for i in range(len(self.items)):
                item = self.items[i]
                if item:
                    if self._item_found(item, name):
                        self._set_item_value_by_key(item, 'declaration_file', declaration_file)
                        self._set_item_value_by_key(item, 'implementation_file', implementation_file)

    def init(self):
        local_print(sys._getframe().f_code.co_name)
        self._process_items()

    def configure(self, configs):
        local_print(sys._getframe().f_code.co_name)
        for config in configs:
            self._update_item_by_config(config)

    def _add_key_value_to_mapping(self, key, value, mapping):
        local_print(sys._getframe().f_code.co_name)
        if key:
            if key not in mapping.keys():
                mapping[key] = []
            if value:
                mapping[key].append(value)

    def _file_maps_items(self):
        local_print(sys._getframe().f_code.co_name)
        self.file_items_mapping = {}
        for item in self.items:
            if item:
                item_name                 = self._get_item_value_by_key('name', item)
                item_declaration_file     = self._get_item_value_by_key('declaration_file', item)
                item_implementation_file  = self._get_item_value_by_key('implementation_file', item)
                self._add_key_value_to_mapping(item_declaration_file, item_name, self.file_items_mapping)
                self._add_key_value_to_mapping(item_implementation_file, item_name, self.file_items_mapping)

    def _get_item_by_name(self, name):
        for item in self.items:
            if item:
                item_name = self._get_item_value_by_key('name', item)
                if item_name == name:
                    return item
        return None

    def _is_declaration_file(self, filename):
        is_declaration_file = False
        if filename.endswith('.h'):
            is_declaration_file = True

        return is_declaration_file

    def _is_implementation_file(self, filename):
        is_implementation_file = False
        if filename.endswith('.c'):
            is_implementation_file = True

        return is_implementation_file

    def _c_head_file_once(self, filename, start=False):
        head_start = None
        head_end   = None
        if filename and len(filename.strip()) > 0:
            if self._is_declaration_file(filename):
                filename      = filename.strip().replace('.', '_')
                filename_once = filename.upper()
                if start:
                    head_start = f'#ifndef {filename_once}{self.crlf}#define {filename_once}{self.crlf}{self.crlf}'
                else:
                    head_end   = f'{self.crlf}#endif/* End of {filename_once} */'

        if start:
            return head_start
        else:
            return head_end

    def _write_value_to_key_file(self, filename, item_names):
        local_print(sys._getframe().f_code.co_name)
        with open(filename, 'w') as w:
            declarations = []
            implementations = []
            head_start = self._c_head_file_once(w.name, True)
            head_end   = self._c_head_file_once(w.name, False)
            includes   = self._get_includes_by_filename(w.name)
            if head_start:
                w.write(head_start)
            if includes:
                w.write(includes)
                w.write(self.crlf)
            for item_name in item_names:
                item                 = self._get_item_by_name(item_name)
                item_declaration     = self._get_item_value_by_key('declaration', item)
                item_implementation  = self._get_item_value_by_key('implementation', item)
                item_scope           = self._get_item_value_by_key('scope', item)
                if item_scope and item_scope.strip() == self.local_inline.strip():
                    implementations.insert(0, item_declaration)
                elif item_declaration and self._is_declaration_file(w.name):
                    declarations.append(item_declaration)
                if item_implementation and self._is_implementation_file(w.name):
                    implementations.append(item_implementation)
            for declaration in declarations:
                if self._is_declaration_file(w.name):
                    print('-----------------> '+w.name)
                    print('-----------------> '+declaration)
                    w.write(declaration)
            for implementation in implementations:
                if self._is_implementation_file(w.name):
                    print('=================> '+w.name)
                    print('=================> '+implementation)
                    w.write(self.crlf)
                    w.write(implementation)
            if head_end:
                w.write(head_end)


    def _process_file_maps_items(self):
        local_print(sys._getframe().f_code.co_name)
        for key in self.file_items_mapping.keys():
            if key:
                self._write_value_to_key_file(key, self.file_items_mapping[key])

    def process(self):
        local_print(sys._getframe().f_code.co_name)
        self._file_maps_items()
        self._process_file_maps_items()

    def print_items(self):
        for item in self.items:
            local_print(item)
        local_print('output mappings')
        local_print(self.file_items_mapping)

def main():
    #local_print(sys._getframe().f_code.co_name)
    configs = [
            { 'name': 'init', 'declaration_file': 'settingservice_manager_test.h', 'implementation_file': 'settingservice_manager_test.c', },
            ]
    car = CarService()
    car.init()
    car.configure(configs)
    car.process()
    car.print_items()

if '__main__' == __name__:
    main()
