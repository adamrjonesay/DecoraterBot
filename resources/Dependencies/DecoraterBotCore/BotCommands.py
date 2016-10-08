# coding=utf-8
"""
The MIT License (MIT)

Copyright (c) 2015-2016 AraHaan

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from __future__ import unicode_literals

import asyncio
import ctypes
import io
import json
import os.path
import platform
import random
import subprocess
import sys
import traceback
try:
    import BotPMError
except ImportError:
    print('Some Unknown thing happened which made a critical bot code file unable to be found.')
import discord
import BotConfigReader
try:
    import TinyURL
    disabletinyurl = False
except ImportError:
    print_data_001 = 'TinyURL for Python 3.x was not installed.\n'
    print_data_002 = 'It can be found at: https://github.com/AraHaan/TinyURL\n'
    print_data_003 = 'Disabled the tinyurl command for now.'
    print(print_data_001 + print_data_002 + print_data_003)
    disabletinyurl = True


class BotData:
    """
        This class is for Internal use only!!!
    """
    def __init__(self):
        self.sepa = os.sep
        self.bits = ctypes.sizeof(ctypes.c_voidp)
        self.platform2 = None
        if self.bits == 4:
            self.platform2 = 'x86'
        elif self.bits == 8:
            self.platform2 = 'x64'
        self.path = sys.path[0]
        if self.path.find('\\AppData\\Local\\Temp') != -1:
            self.path = sys.executable.strip(
                'DecoraterBot.{0}.{1}.{2.name}-{3.major}{3.minor}{3.micro}.exe'.format(self.platform2, sys.platform,
                                                                                       sys.implementation,
                                                                                       sys.version_info))
        self.PY35 = sys.version_info >= (3, 5)
        try:
            self.consoledatafile = io.open('{0}{1}resources{1}ConfigData{1}ConsoleWindow.json'.format(self.path,
                                                                                                      self.sepa))
            self.consoletext = json.load(self.consoledatafile)
            self.consoledatafile.close()
        except FileNotFoundError:
            print('ConsoleWindow.json is not Found. Cannot Continue.')
            sys.exit(2)
        self.disabletinyurl = disabletinyurl
        self.botbanslist = io.open('{0}{1}resources{1}ConfigData{1}BotBanned.json'.format(self.path, self.sepa))
        self.banlist = json.load(self.botbanslist)
        self.botbanslist.close()
        try:
            self.commandslist = io.open('{0}{1}resources{1}ConfigData{1}BotCommands.json'.format(self.path,
                                                                                                 self.sepa))
            self.commandlist = json.load(self.commandslist)
            self.commandslist.close()
        except FileNotFoundError:
            print(str(self.consoletext['Missing_JSON_Errors'][3]))
            sys.exit(2)
        try:
            self.botmessagesdata = io.open('{0}{1}resources{1}ConfigData{1}BotMessages.json'.format(self.path,
                                                                                                    self.sepa))
            self.botmessages = json.load(self.botmessagesdata)
            self.botmessagesdata.close()
        except FileNotFoundError:
            print(str(self.consoletext['Missing_JSON_Errors'][1]))
            sys.exit(2)
        self.version = str(self.consoletext['WindowVersion'][0])
        self.rev = str(self.consoletext['Revision'][0])
        self.sourcelink = str(self.botmessages['source_command_data'][0])
        self.othercommands = str(self.botmessages['commands_command_data'][1])
        self.commandstuff = str(self.botmessages['commands_command_data'][4])
        self.botcommands = str(self.botmessages['commands_command_data'][0]) + self.othercommands + self.commandstuff
        self.botcommands_without_other_stuff = str(self.botmessages['commands_command_data'][0]) + self.othercommands
        self.othercommandthings = str(self.botmessages['commands_command_data'][4]) + str(
            self.botmessages['commands_command_data'][5])
        self.botcommandswithturl_01 = str(self.botmessages['commands_command_data'][3]) + self.othercommandthings
        self.botcommandswithtinyurl = self.botcommands_without_other_stuff + self.botcommandswithturl_01
        self.changelog = str(self.botmessages['changelog_data'][0])
        self.info = "``" + str(self.consoletext['WindowName'][0]) + self.version + self.rev + "``"
        self.botcommandsPM = str(self.botmessages['commands_command_data'][2])
        self.commandturlfix = str(self.botmessages['commands_command_data'][5])
        self.botcommandsPMwithtinyurl = self.botcommandsPM + str(
            self.botmessages['commands_command_data'][3]) + self.commandturlfix
        self.PATH = '{0}{1}resources{1}ConfigData{1}Credentials.json'.format(self.path, self.sepa)
        self._log_games = True
        if os.path.isfile(self.PATH) and os.access(self.PATH, os.R_OK):
            self.BotConfig = BotConfigReader.BotConfigVars()
            self._log_games = self.BotConfig.log_games
            self.owner_id = self.BotConfig.discord_user_id
            if self.owner_id == 'None':
                self.owner_id = None
            self._is_official_bot = self.BotConfig.is_official_bot
            self._pm_commands_list = self.BotConfig.pm_commands_list
            self._bot_prefix = self.BotConfig.bot_prefix
        self.sent_prune_error_message = False
        self.tinyurlerror = False
        self.link = None
        if self._log_games:
            import BotLogs
            self.DBLogs = BotLogs.BotLogs()

    @asyncio.coroutine
    def attack_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'attack'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                for user in message.mentions:
                    yield from client.send_message(user, str(self.botmessages['attack_command_data'][0]))
                    break
                else:
                    yield from client.send_message(message.author, str(self.botmessages['attack_command_data'][1]))

    @asyncio.coroutine
    def randomcoin_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'coin'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                msg = random.randint(0, 1)
                if msg == 0:
                    heads_coin = "{0}{1}resources{1}images{1}coins{1}Heads.png".format(self.path, self.sepa)
                    try:
                        yield from client.send_file(message.channel, heads_coin)
                    except discord.errors.Forbidden:
                        try:
                            message_data = str(self.botmessages['coin_command_data'][0])
                            yield from client.send_message(message.channel, message_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                if msg == 1:
                    tails_coin = "{0}{1}resources{1}images{1}coins{1}Tails.png".format(self.path, self.sepa)
                    try:
                        yield from client.send_file(message.channel, tails_coin)
                    except discord.errors.Forbidden:
                        try:
                            message_data = str(self.botmessages['coin_command_data'][0])
                            yield from client.send_message(message.channel, message_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def colors_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'color'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                if self._bot_prefix + "pink" in message.content:
                    desrole = message.content[len(self._bot_prefix + "color " + self._bot_prefix + "pink "):].strip()
                    role2 = discord.utils.find(lambda role: role.name == desrole, message.channel.server.roles)
                    try:
                        yield from client.edit_role(message.channel.server, role2, color=discord.Colour(int(
                            'ff3054', 16)))
                    except discord.errors.Forbidden:
                        try:
                            message_data = str(self.botmessages['color_command_data'][0])
                            yield from client.send_message(message.channel, message_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    except discord.errors.HTTPException:
                        return
                    except AttributeError:
                        return
                if self._bot_prefix + "brown" in message.content:
                    desrole = message.content[len(self._bot_prefix + "color " + self._bot_prefix + "brown "):].strip()
                    role2 = discord.utils.find(lambda role: role.name == desrole, message.channel.server.roles)
                    try:
                        yield from client.edit_role(message.channel.server, role2, color=discord.Colour(int(
                            '652d2d', 16)))
                    except discord.errors.Forbidden:
                        try:
                            message_data = str(self.botmessages['color_command_data'][0])
                            yield from client.send_message(message.channel, message_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    except discord.errors.HTTPException:
                        return
                    except AttributeError:
                        return

    @asyncio.coroutine
    def debug_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'eval'):
            if message.author.id == self.owner_id:
                debugcode = message.content[len(self._bot_prefix + "eval "):].strip()
                if debugcode.rfind('yield from client.send_message(message.channel, ') is not -1:
                    debugcode = debugcode[len("yield from client.send_message(message.channel, "):].strip()
                    debugcode = debugcode.strip(")")
                    if debugcode.find("'") is not -1:
                        debugcode = debugcode.strip("'")
                    elif debugcode.find('"') is not -1:
                        debugcode = debugcode.strip('"')
                    if debugcode.find('message.author.mention') is not -1:
                        debugcode = debugcode.replace('message.author.mention + "', message.author.mention)
                    yield from client.send_message(message.channel, debugcode)
                else:
                    botowner = discord.utils.find(lambda member: member.id == self.owner_id,
                                                  message.channel.server.members)
                    try:
                        try:
                            debugcode = eval(debugcode)
                        except SystemExit:
                            pass
                        debugcode = "```py\n" + str(debugcode) + "\n```"
                        try:
                            yield from client.send_message(message.channel, debugcode)
                        except discord.errors.Forbidden:
                            msgdata = str(self.botmessages['eval_command_data'][0])
                            message_data = msgdata.format(message.channel.server.name, message.channel.name)
                            yield from client.send_message(botowner, message_data)
                            yield from client.send_message(botowner, debugcode)
                        except discord.errors.HTTPException:
                            if len(debugcode) > 2000:
                                result_info = str(self.botmessages['eval_command_data'][1])
                                yield from client.send_message(message.channel, result_info)
                    except Exception as e:
                        str(e)
                        debugcode = traceback.format_exc()
                        debugcode = str(debugcode)
                        try:
                            yield from client.send_message(message.channel, "```py\n" + debugcode + "\n```")
                        except discord.errors.Forbidden:
                            msgdata = str(self.botmessages['eval_command_data'][0])
                            message_data = msgdata.format(message.channel.server.name, message.channel.name)
                            yield from client.send_message(botowner, message_data)
                            yield from client.send_message(botowner, "```py\n" + debugcode + "\n```")
            else:
                try:
                    result_info = str(self.botmessages['eval_command_data'][2])
                    yield from client.send_message(message.channel, result_info)
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'debug'):
            # makes the owner AKA Creator of the bot only able to use this as this can be dangerous.
            if message.author.id == self.owner_id:
                debugcode_new = "# coding=utf-8\n" + message.content[len(self._bot_prefix + "debug "):].strip()
                botowner = discord.utils.find(lambda member: member.id == self.owner_id, message.channel.server.members)
                try:
                    evalcodefile = '{0}{1}resources{1}exec_files{1}exec_temp.py'.format(self.path, self.sepa)
                    eval_temp_code = io.open(evalcodefile, 'w+', encoding='utf-8')
                    debugcode_new += '\n'
                    eval_temp_code.write(debugcode_new)
                    eval_temp_code.close()
                    execoutputfile = '{0}{1}resources{1}exec_files{1}exec_output_temp.txt'.format(self.path, self.sepa)
                    eval_temp_result_output = io.open(execoutputfile, 'w', encoding='utf-8')
                    out = eval_temp_result_output
                    p = subprocess.Popen("{0}{1}python {2}".format(sys.path[4], self.sepa, evalcodefile), stdout=out,
                                         stderr=out, shell=True)
                    p.wait()
                    eval_temp_result_output.close()
                    eval_temp_result_read = io.open(execoutputfile, encoding='utf-8')
                    eval_result = eval_temp_result_read.read()
                    if eval_result is not '':
                        debugcode = eval_result
                    else:
                        debugcode = 'None'
                    eval_temp_result_read.close()
                    try:
                        yield from client.send_message(message.channel, "```py\n" + debugcode + "\n```")
                    except discord.errors.Forbidden:
                        msgdata = str(self.botmessages['eval_command_data'][0])
                        message_data = msgdata.format(message.channel.server.name, message.channel.name)
                        yield from client.send_message(botowner, message_data)
                        yield from client.send_message(botowner, "```py\n" + debugcode + "\n```")
                    except discord.errors.HTTPException:
                        if len(debugcode) > 2000:
                            result_info = str(self.botmessages['eval_command_data'][1])
                            yield from client.send_message(message.channel, result_info)
                except Exception as e:
                    str(e)
                    debugcode = traceback.format_exc()
                    debugcode = str(debugcode)
                    try:
                        yield from client.send_message(message.channel, "```py\n" + debugcode + "\n```")
                    except discord.errors.Forbidden:
                        msgdata = str(self.botmessages['eval_command_data'][0])
                        message_data = msgdata.format(message.channel.server.name, message.channel.name)
                        yield from client.send_message(botowner, message_data)
                        yield from client.send_message(botowner, "```py\n" + debugcode + "\n```")
            else:
                try:
                    result_info = str(self.botmessages['debug_command_data'][0])
                    yield from client.send_message(message.channel, result_info)
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def games_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'game'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                desgame = message.content[len(self._bot_prefix + "game "):].strip()
                desgametype = None
                stream_url = None
                if len(desgame) > 0:
                    if len(message.mentions) > 0:
                        for x in message.mentions:
                            desgame = desgame.replace(x.mention, x.name)
                    desgame = str(desgame)
                    if desgame.find(" | type=") is not -1:
                        if desgame.find(" | type=1") is not -1:
                            desgame = desgame.replace(" | type=1", "")
                            desgametype = 1
                            stream_url = "https://twitch.tv/decoraterbot"
                        elif desgame.find(" | type=2") is not -1:
                            desgame = desgame.replace(" | type=2", "")
                            desgametype = 2
                            stream_url = "https://twitch.tv/decoraterbot"
                    if desgametype is not None:
                        if self._log_games:
                            self.DBLogs.gamelog(message, desgame)
                        yield from client.change_presence(game=discord.Game(name=desgame, type=desgametype,
                                                                            url=stream_url))
                        try:
                            msgdata = str(self.botmessages['game_command_data'][0]).format(desgame)
                            message_data = msgdata.replace("idle", "streaming")
                            yield from client.send_message(message.channel, message_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    else:
                        if self._log_games:
                            self.DBLogs.gamelog(message, desgame)
                        yield from client.change_presence(game=discord.Game(name=desgame), idle=True)
                        try:
                            msgdata = str(self.botmessages['game_command_data'][0]).format(desgame)
                            message_data = msgdata
                            yield from client.send_message(message.channel, message_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'remgame'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                game_name = str(self.consoletext['On_Ready_Game'][0])
                stream_url = "https://twitch.tv/decoraterbot"
                yield from client.change_presence(game=discord.Game(name=game_name, type=1, url=stream_url))
                try:
                    yield from client.send_message(message.channel, str(self.botmessages['remgame_command_data'][0]))
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def invite_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'join'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                if self._is_official_bot:
                    yield from client.send_message(message.channel, str(self.botmessages['join_command_data'][3]))
                else:
                    code = message.content[len(self._bot_prefix + "join "):].strip()
                    if code == '':
                        url = None
                    else:
                        url = code
                    if url is not None:
                        try:
                            yield from client.accept_invite(url)
                            msg_data = str(self.botmessages['join_command_data'][0])
                            yield from client.send_message(message.channel, msg_data)
                        except discord.errors.NotFound:
                            msg_data = str(self.botmessages['join_command_data'][1])
                            yield from client.send_message(message.channel, msg_data)
                    else:
                        yield from client.send_message(message.channel, str(self.botmessages['join_command_data'][2]))

    @asyncio.coroutine
    def kills_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'kill'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                data = message.content[len(self._bot_prefix + "kill "):].strip()
                if message.channel.is_private:
                    msg = random.randint(1, 4)
                    if msg == 1:
                        message_data = str(self.botmessages['kill_command_data'][0]).format(message.author)
                        yield from client.send_message(message.channel, message_data)
                    if msg == 2:
                        message_data = str(self.botmessages['kill_command_data'][1]).format(message.author)
                        yield from client.send_message(message.channel, message_data)
                    if msg == 3:
                        message_data = str(self.botmessages['kill_command_data'][2]).format(message.author)
                        yield from client.send_message(message.channel, message_data)
                    if msg == 4:
                        message_data = str(self.botmessages['kill_command_data'][3]).format(message.author)
                        yield from client.send_message(message.channel, message_data)
                else:
                    if data.rfind(client.user.name) != -1:
                        try:
                            msg_data = str(self.botmessages['kill_command_data'][4])
                            yield from client.send_message(message.channel, msg_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    else:
                        msg = random.randint(1, 4)
                        for disuser in message.mentions:
                            if message.author == disuser:
                                try:
                                    msg_data = str(self.botmessages['kill_command_data'][4])
                                    yield from client.send_message(message.channel, msg_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                                break
                            if client.user == disuser:
                                try:
                                    msg_data = str(self.botmessages['kill_command_data'][4])
                                    yield from client.send_message(message.channel, msg_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                                break
                            user = discord.utils.find(lambda member: member.name == disuser.name,
                                                      message.channel.server.members)
                            if msg == 1:
                                try:
                                    msgdata = str(self.botmessages['kill_command_data'][5]).format(message.author, user)
                                    message_data = msgdata
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                                break
                            if msg == 2:
                                try:
                                    msgdata = str(self.botmessages['kill_command_data'][6]).format(message.author, user)
                                    message_data = msgdata
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                                break
                            if msg == 3:
                                try:
                                    msgdata = str(self.botmessages['kill_command_data'][7]).format(message.author, user)
                                    message_data = msgdata
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                                break
                            if msg == 4:
                                try:
                                    msgdata = str(self.botmessages['kill_command_data'][8]).format(message.author, user)
                                    message_data = msgdata
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                                break
                        else:
                            if msg == 1:
                                try:
                                    message_data = str(self.botmessages['kill_command_data'][0]).format(message.author)
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                            if msg == 2:
                                try:
                                    message_data = str(self.botmessages['kill_command_data'][1]).format(message.author)
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                            if msg == 3:
                                try:
                                    message_data = str(self.botmessages['kill_command_data'][2]).format(message.author)
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                            if msg == 4:
                                try:
                                    message_data = str(self.botmessages['kill_command_data'][3]).format(message.author)
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def bot_mentioned_helper(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.author.id in self.banlist['Users']:
            return
        elif message.author.bot:
            return
        else:
            pref = self._bot_prefix
            unig = 'unignorechannel'
            # Allows Joining a Voice Channel.
            # This is handling if some idiot mentions the bot with this command in it.
            # This also bypasses the PEP 8 Bullshit.
            jovo = pref + 'JoinVoiceChannel'
            if message.content.startswith(pref + 'kill') or message.content.startswith(pref + 'changelog'):
                return
            elif message.content.startswith(pref + 'raid') or message.content.startswith(pref + 'source'):
                return
            elif message.content.startswith(pref + 'prune') or message.content.startswith(pref + 'game'):
                return
            elif message.content.startswith(pref + 'remgame') or message.content.startswith(pref + 'join'):
                return
            elif message.content.startswith(pref + 'update') or message.content.startswith(pref + 'say'):
                return
            elif message.content.startswith(pref + 'type') or message.content.startswith(pref + 'uptime'):
                return
            elif message.content.startswith(pref + 'reload') or message.content.startswith(pref + 'pyversion'):
                return
            elif message.content.startswith(pref + 'Libs') or message.content.startswith(pref + 'userinfo'):
                return
            elif message.content.startswith(pref + 'kick') or message.content.startswith(pref + 'ban'):
                return
            elif message.content.startswith(pref + 'softban') or message.content.startswith(pref + 'clear'):
                return
            elif message.content.startswith(pref + 'ignorechannel') or message.content.startswith(pref + unig):
                return
            elif message.content.startswith(pref + 'tinyurl') or message.content.startswith(jovo):
                return
            elif message.content.startswith(pref + 'play') or message.content.startswith(pref + 'pause'):
                return
            elif message.content.startswith(pref + 'unpause') or message.content.startswith(pref + 'stop'):
                return
            elif message.content.startswith(pref + 'move') or message.content.startswith(pref + 'LeaveVoiceChannel'
                                                                                         ):
                return
            elif message.content.startswith(pref + 'Playlist'):
                return
            else:
                if message.channel.server.id == "140849390079180800":
                    return
                elif message.author.id == client.user.id:
                    return
                elif message.channel.server.id == "110373943822540800":
                    if message.author.id == "103607047383166976":
                        return
                    else:
                        info2 = str(self.botmessages['On_Bot_Mention_Message_Data'][0]).format(message.author)
                        yield from client.send_message(message.channel, info2)
                elif message.channel.server.id == '101596364479135744':
                    if message.author.id == "110368240768679936":
                        return
                    else:
                        info2 = str(self.botmessages['On_Bot_Mention_Message_Data'][0]).format(message.author)
                        yield from client.send_message(message.channel, info2)
                else:
                    info2 = str(self.botmessages['On_Bot_Mention_Message_Data'][0]).format(message.author)
                    try:
                        yield from client.send_message(message.channel, info2)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def mention_ban_helper(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.author.id == client.user.id:
            return
        if message.channel.server.id == "105010597954871296":
            return
        if message.author.id == self.owner_id:
            return
        else:
            try:
                yield from client.ban(message.author)
                try:
                    message_data = str(self.botmessages['mention_spam_ban'][0]).format(message.author)
                    yield from client.send_message(message.channel, message_data)
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)
            except discord.errors.Forbidden:
                try:
                    msgdata = str(self.botmessages['mention_spam_ban'][1]).format(message.author)
                    message_data = msgdata
                    yield from client.send_message(message.channel, message_data)
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)
            except discord.HTTPException:
                try:
                    msgdata = str(self.botmessages['mention_spam_ban'][2]).format(message.author)
                    message_data = msgdata
                    yield from client.send_message(message.channel, message_data)
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def mod_commands_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if len(message.mentions) > 5:
            yield from self.mention_ban_helper(client, message)
        if message.content.startswith(self._bot_prefix + "ban"):
            role2 = discord.utils.find(lambda role: role.name == 'Bot Commander', message.channel.server.roles)
            if role2 in message.author.roles:
                for disuser in message.mentions:
                    listdata = message.channel.server.members
                    member2 = discord.utils.find(lambda member: member.name == disuser.name, listdata)
                    try:
                        yield from client.ban(member2, delete_message_days=7)
                        try:
                            message_data = str(self.botmessages['ban_command_data'][0]).format(member2)
                            yield from client.send_message(message.channel, message_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    except discord.Forbidden:
                        try:
                            yield from client.send_message(message.channel, str(
                                self.botmessages['ban_command_data'][1]))
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    except discord.HTTPException:
                        try:
                            yield from client.send_message(message.channel, str(
                                self.botmessages['ban_command_data'][2]))
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    break
                else:
                    try:
                        yield from client.send_message(message.channel, str(self.botmessages['ban_command_data'][3]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
            else:
                try:
                    yield from client.send_message(message.channel, str(self.botmessages['ban_command_data'][4]))
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + "softban"):
            role2 = discord.utils.find(lambda role: role.name == 'Bot Commander', message.channel.server.roles)
            if role2 in message.author.roles:
                for disuser in message.mentions:
                    memberlist = message.channel.server.members
                    member2 = discord.utils.find(lambda member: member.name == disuser.name, memberlist)
                    try:
                        yield from client.ban(member2, delete_message_days=7)
                        yield from client.unban(member2.server, member2)
                        try:
                            message_data = str(self.botmessages['softban_command_data'][0]).format(member2)
                            yield from client.send_message(message.channel, message_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    except discord.Forbidden:
                        try:
                            msg_data = str(self.botmessages['softban_command_data'][1])
                            yield from client.send_message(message.channel, msg_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    except discord.HTTPException:
                        try:
                            msg_data = str(self.botmessages['softban_command_data'][2])
                            yield from client.send_message(message.channel, msg_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    break
                else:
                    try:
                        yield from client.send_message(message.channel, str(
                            self.botmessages['softban_command_data'][3]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
            else:
                try:
                    yield from client.send_message(message.channel, str(self.botmessages['softban_command_data'][4]))
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + "kick"):
            role2 = discord.utils.find(lambda role: role.name == 'Bot Commander', message.channel.server.roles)
            if role2 in message.author.roles:
                for disuser in message.mentions:
                    memberlist = message.channel.server.members
                    member2 = discord.utils.find(lambda member: member.name == disuser.name, memberlist)
                    try:
                        yield from client.kick(member2)
                        try:
                            message_data = str(self.botmessages['kick_command_data'][0]).format(member2)
                            yield from client.send_message(message.channel, message_data)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    except discord.Forbidden:
                        try:
                            yield from client.send_message(message.channel, str(
                                self.botmessages['kick_command_data'][1]))
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    except discord.HTTPException:
                        try:
                            yield from client.send_message(message.channel, str(
                                self.botmessages['kick_command_data'][2]))
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    break
                else:
                    try:
                        yield from client.send_message(message.channel, str(self.botmessages['kick_command_data'][3]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
            else:
                try:
                    yield from client.send_message(message.channel, str(self.botmessages['kick_command_data'][4]))
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def other_commands_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'commands'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                if message.channel.is_private:
                    if self.disabletinyurl:
                        yield from client.send_message(message.channel, self.botcommandsPM)
                    else:
                        yield from client.send_message(message.channel, self.botcommandsPMwithtinyurl)
                else:
                    if self.disabletinyurl:
                        try:
                            if self._pm_commands_list:
                                yield from client.send_message(message.author, self.botcommands)
                            else:
                                yield from client.send_message(message.channel, self.botcommands)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
                    else:
                        try:
                            if self._pm_commands_list:
                                yield from client.send_message(message.author, self.botcommandswithtinyurl)
                                msgdata = str(self.botmessages['commands_command_data'][6])
                                message_data = msgdata.format(message.author.mention)
                                try:
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                            else:
                                yield from client.send_message(message.channel, self.botcommandswithtinyurl)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'changelog'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                try:
                    yield from client.send_message(message.channel, self.changelog.format(self.version + self.rev))
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'raid'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                if message.channel.is_private:
                    return
                else:
                    result = message.content.replace("::raid", "")
                    if result.startswith(" "):
                        result = result[len(" "):].strip()
                    try:
                        message_data = str(self.botmessages['raid_command_data'][0]).format(result)
                        yield from client.send_message(message.channel, message_data)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'update'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                if message.channel.is_private:
                    return
                else:
                    try:
                        yield from client.send_message(message.channel,
                                                       str(self.botmessages['update_command_data'][0]).format(
                                                           self.info))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'Libs'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                libs = str(self.botmessages['Libs_command_data'][0])
                try:
                    yield from client.send_message(message.channel, libs)
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'source'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                try:
                    msgdata = self.sourcelink.format(message.author)
                    message_data = msgdata
                    yield from client.send_message(message.channel, message_data)
                except discord.errors.Forbidden:
                    yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'type'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                yield from client.send_typing(message.channel)
        if message.content.startswith(self._bot_prefix + 'pyversion'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                if message.channel.is_private:
                    return
                else:
                    python_platform = None
                    if self.bits == 8:
                        python_platform = "64-Bit"
                    elif self.bits == 4:
                        python_platform = "32-Bit"
                    vers = "```py\nPython v{0} {1}```".format(platform.python_version(), python_platform)
                    try:
                        yield from client.send_message(message.channel, vers)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'AgarScrub'):
            try:
                reply = 'https://imgflip.com/i/12yq2n'
                yield from client.send_message(message.channel, reply)
            except discord.errors.Forbidden:
                yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'stats'):
            server_count = str(len(client.servers))
            member_count = str(len(set([member for member in client.get_all_members()])))
            textchannels_count = str(len(set(
                [channel for channel in client.get_all_channels() if channel.type == discord.ChannelType.text])))
            formatted_data = str(
                self.botmessages['stats_command_data'][0]).format(server_count, member_count, textchannels_count)
            yield from client.send_message(message.channel, formatted_data)
        if message.content.startswith(self._bot_prefix + 'rs'):
            filename1 = '{0}{1}resources{1}images{1}elsword{1}RS.jpg'.format(self.path, self.sepa)
            file_object = open(filename1, 'rb')
            file_data = None
            if file_object is not None:
                file_data = file_object.read()
                file_object.close()
            yield from client.edit_profile(avatar=file_data)
        if message.content.startswith(self._bot_prefix + 'as'):
            filename2 = '{0}{1}resources{1}images{1}elsword{1}AS.jpg'.format(self.path, self.sepa)
            file_object = open(filename2, 'rb')
            file_data = None
            if file_object is not None:
                file_data = file_object.read()
                file_object.close()
            yield from client.edit_profile(avatar=file_data)
        if message.content.startswith(self._bot_prefix + 'ai'):
            filename3 = '{0}{1}resources{1}images{1}elsword{1}AI.jpg'.format(self.path, self.sepa)
            file_object = open(filename3, 'rb')
            file_data = None
            if file_object is not None:
                file_data = file_object.read()
                file_object.close()
            yield from client.edit_profile(avatar=file_data)
        if message.content.startswith(self._bot_prefix + 'lk'):
            filename4 = '{0}{1}resources{1}images{1}elsword{1}LK.jpg'.format(self.path, self.sepa)
            file_object = open(filename4, 'rb')
            file_data = None
            if file_object is not None:
                file_data = file_object.read()
                file_object.close()
            yield from client.edit_profile(avatar=file_data)
        if message.content.startswith(self._bot_prefix + 'vp'):
            filename5 = '{0}{1}resources{1}images{1}elsword{1}VP.jpg'.format(self.path, self.sepa)
            file_object = open(filename5, 'rb')
            file_data = None
            if file_object is not None:
                file_data = file_object.read()
                file_object.close()
            yield from client.edit_profile(avatar=file_data)
        if message.content.startswith(self._bot_prefix + 'ws'):
            filename6 = '{0}{1}resources{1}images{1}elsword{1}WS.jpg'.format(self.path, self.sepa)
            file_object = open(filename6, 'rb')
            file_data = None
            if file_object is not None:
                file_data = file_object.read()
                file_object.close()
            yield from client.edit_profile(avatar=file_data)
        if message.content.startswith(self._bot_prefix + 'meme'):
            desdata = message.content[len(self._bot_prefix + 'meme'):].strip()
            meme_error = False
            desdata = str(desdata)
            toptext = None
            bottext = None
            pic = None
            msg_mention_list_len = len(message.mentions) - 1
            if msg_mention_list_len == -1:
                msg_mention_list_len = 0
            if msg_mention_list_len > 0:
                if desdata.startswith(message.mentions[msg_mention_list_len].mention):
                    desdata = desdata.replace(" | ", "\n").replace('-', '--').replace(' ', '-')
                    desdata = desdata.splitlines()
                    try:
                        pic = message.mentions[msg_mention_list_len].avatar_url
                    except IndexError:
                        meme_error = True
                        msgdata = str(self.botmessages['meme_command_data'][0])
                        yield from client.send_message(message.channel, msgdata)
                    if not meme_error:
                        try:
                            toptext = desdata[1].replace('_', '__').replace('?', '~q').replace(
                                '%', '~p').replace('#', '~h').replace('/', '~s')
                            for x in message.mentions:
                                toptext = toptext.replace(x.mention, x.name)
                            toptext = toptext.replace('<', '').replace('>', '').replace('@', '')
                        except IndexError:
                            meme_error = True
                            msgdata = str(self.botmessages['meme_command_data'][1])
                            yield from client.send_message(message.channel, msgdata)
                    if not meme_error:
                        try:
                            bottext = desdata[2].replace('_', '__').replace(
                                '?', '~q').replace('%', '~p').replace('#', '~h').replace('/', '~s')
                            for x in message.mentions:
                                bottext = bottext.replace(x.mention, x.name)
                            bottext = bottext.replace('<', '').replace('>', '').replace('@', '')
                        except IndexError:
                            meme_error = True
                            msgdata = str(self.botmessages['meme_command_data'][2])
                            yield from client.send_message(message.channel, msgdata)
                    if not meme_error:
                        rep = "http://memegen.link/custom/{0}/{1}.jpg?alt={2}".format(toptext, bottext, pic)
                        yield from client.send_message(message.channel, rep)
            else:
                desdata = desdata.replace(" | ", "\n").replace('-', '--').replace(' ', '-')
                desdata = desdata.splitlines()
                try:
                    pic = str(desdata[0])
                except IndexError:
                    meme_error = True
                    msgdata = str(self.botmessages['meme_command_data'][0])
                    yield from client.send_message(message.channel, msgdata)
                if not meme_error:
                    try:
                        toptext = desdata[1].replace('_', '__').replace('?', '~q').replace(
                            '%', '~p').replace('#', '~h').replace('/', '~s')
                        for x in message.mentions:
                            toptext = toptext.replace(x.mention, x.name)
                        toptext = toptext.replace('<', '').replace('>', '').replace('@', '')
                    except IndexError:
                        meme_error = True
                        msgdata = str(self.botmessages['meme_command_data'][1])
                        yield from client.send_message(message.channel, msgdata)
                if not meme_error:
                    try:
                        bottext = desdata[2].replace('_', '__').replace('?', '~q').replace(
                            '%', '~p').replace('#', '~h').replace('/', '~s')
                        for x in message.mentions:
                            bottext = bottext.replace(x.mention, x.name)
                        bottext = bottext.replace('<', '').replace('>', '').replace('@', '')
                    except IndexError:
                        meme_error = True
                        msgdata = str(self.botmessages['meme_command_data'][2])
                        yield from client.send_message(message.channel, msgdata)
                if not meme_error:
                    rep = "http://memegen.link/{0}/{1}/{2}.jpg".format(pic, toptext, bottext)
                    yield from client.send_message(message.channel, rep)
        if message.content.startswith(self._bot_prefix + 'givecreds'):
            """
                This command tricks a bot to giving the owner of this bot 200 credits.
            """
            ownermentiondata = '<@' + self.owner_id + '>'
            yield from client.send_message(message.channel, 't!daily {0}'.format(ownermentiondata))
        """
            This below is left in so anyone could have a example of itterating through roles to find the right one
            that they want.

            Note: This uses the json module to load up ppl who was listed in a json file that cannot use the bot.

            This does also only send 1 message after it gets the entire role list consisting of the role name
            and it's id.

            if message.content.startswith(_bot_prefix + 'roleinfo'):
                roleinfo = None
                if message.author.id in banlist['Users']:
                    message_data = " Due to Continuous abuse you have been Bot Banned."
                    yield from client.send_message(message.channel, message.author.mention + message_data)
                else:
                    for role in message.channel.server.roles:
                        if roleinfo is None:
                            roleinfo = "role name: {0}, role id: {1}\n".format(role.name, role.id)
                        else:
                            roleinfo += "role name: {0}, role id: {1}\n".format(role.name, role.id)
                    yield from client.send_message(message.channel, "```" + roleinfo + "```")
            """

    # Sorry guys if you have python 3.5 or 4.6 you can uncomment this.
    # This is because python 3.4 would still detect this as a SyntaxError.
    # if self.PY35:
    #     async def prune_command_iterater_helper(self, client, message, num):
    #         """
    #         Prunes Messages.
    #         :param client: Discord Client.
    #         :param message: Message
    #         :param num:
    #         :return: Nothing.
    #         """
    #         try:
    #             await client.purge_from(message.channel, limit=num + 1)
    #         except discord.HTTPException:
    #             if self.sent_prune_error_message is False:
    #                 self.sent_prune_error_message = True
    #                 await client.send_message(message.channel, str(botmessages['prune_command_data'][0]))
    #             else:
    #                 return

    #     @staticmethod
    #     async def clear_command_iterater_helper(client, message):
    #         """
    #         Clears the bot's messages.
    #         :param client: Discord Client.
    #         :param message: Message.
    #         :return: Nothing.
    #         """
    #         def botauthor(m):
    #             """
    #             Checks if the messages are the bot's messages.
    #             :param m: Messages.
    #             :return: Messages from the bot.
    #             """
    #             return m.author == client.user

    #         try:
    #             await client.purge_from(message.channel, limit=100, check=botauthor)
    #         except discord.HTTPException:
    #             return
    # else:
    # Indent this code as well if you want this to work only in Python 3.5+ as well.
    # Although you do not have to as this Syntax is valid in 3.5+ or should be. the async def is also optional.
    @asyncio.coroutine
    def prune_command_iterater_helper(self, client, message, num):
        """
        Prunes Messages.
        :param self:
        :param client: Discord Client.
        :param message: Message
        :param num:
        :return: Nothing.
        """
        try:
            yield from client.purge_from(message.channel, limit=num + 1)
        except discord.HTTPException:
            if self.sent_prune_error_message is False:
                self.sent_prune_error_message = True
                yield from client.send_message(message.channel, str(self.botmessages['prune_command_data'][0]))
            else:
                return

    @asyncio.coroutine
    def clear_command_iterater_helper(self, client, message):
        """
        Clears the bot's messages.
        :param self:
        :param client: Discord Client.
        :param message: Message.
        :return: Nothing.
        """
        def botauthor(m):
            """
            Checks if the messages are the bot's messages.
            :param m: Messages.
            :return: Messages from the bot.
            """
            return m.author == client.user

        try:
            yield from client.purge_from(message.channel, limit=100, check=botauthor)
        except discord.HTTPException:
            return

    @asyncio.coroutine
    def prune_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'prune'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                self.sent_prune_error_message = False
                role2 = discord.utils.find(lambda role: role.name == 'Bot Commander', message.channel.server.roles)
                """
                if message.author.id == owner_id:
                    opt = message.content[len(_bot_prefix + "prune "):].strip()
                    num = 1
                    if opt:
                        try:
                            num = int(opt)
                        except:
                            return
                    yield from self.prune_command_iterater_helper(client, message, num)
                else:
                """
                if role2 in message.author.roles:
                    opt = message.content[len(self._bot_prefix + "prune "):].strip()
                    num = 1
                    if opt:
                        try:
                            num = int(opt)
                        except Exception as e:
                            str(e)
                            return
                    yield from self.prune_command_iterater_helper(client, message, num)
                else:
                    try:
                        yield from client.send_message(message.channel, str(self.botmessages['prune_command_data'][1]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)

    # Unused but too lazy to remove this.

    @asyncio.coroutine
    def bot_roles_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'giveme'):
            if message.channel.server and message.channel.server.id == "81812480254291968":
                desrole = message.content[len(self._bot_prefix + "giveme "):].strip()
                role2 = discord.utils.find(lambda role: role.name == 'Muted', message.channel.server.roles)
                role3 = discord.utils.find(lambda role: role.name == 'Students', message.channel.server.roles)
                if 'admin' in desrole:
                    if 'Muted' in message.author.roles:
                        yield from client.add_roles(message.author, role2)
                        yield from client.send_message(message.channel, str(self.botmessages['giveme_command_data'][0]))
                    else:
                        yield from client.send_message(message.channel, str(self.botmessages['giveme_command_data'][5]))
                elif 'student' in desrole:
                    if 'Students' in message.author.roles:
                        yield from client.add_roles(message.author, role3)
                        yield from client.send_message(message.channel, str(self.botmessages['giveme_command_data'][1]))
                    else:
                        yield from client.send_message(message.channel, str(self.botmessages['giveme_command_data'][6]))
            else:
                if message.channel.server and message.channel.server.id == "127233852182626304":
                    desrole = message.content[len(self._bot_prefix + "giveme "):].strip()
                    rolelist = message.channel.server.roles
                    role2 = discord.utils.find(lambda role: role.name == '3rd Party Developer', rolelist)
                    role3 = discord.utils.find(lambda role: role.name == 'Streamer', rolelist)
                    if 'dev' in desrole:
                        if role2 not in message.author.roles:
                            yield from client.add_roles(message.author, role2)
                            yield from client.send_message(message.channel, str(
                                self.botmessages['giveme_command_data'][2]))
                        else:
                            yield from client.send_message(message.channel, str(
                                self.botmessages['giveme_command_data'][7]))
                    elif 'stream' in desrole:
                        if role3 not in message.author.roles:
                            yield from client.add_roles(message.author, role3)
                            yield from client.send_message(message.channel, str(
                                self.botmessages['giveme_command_data'][3]))
                        else:
                            yield from client.send_message(message.channel, str(
                                self.botmessages['giveme_command_data'][8]))
                else:
                    try:
                        yield from client.send_message(message.channel, str(
                            self.botmessages['giveme_command_data'][4]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
        if message.content.startswith(self._bot_prefix + 'remove'):
            if message.channel.server and message.channel.server.id == "127233852182626304":
                desrole = message.content[len(self._bot_prefix + "remove "):].strip()
                rolelist = message.channel.server.roles
                role2 = discord.utils.find(lambda role: role.name == '3rd Party Developer', rolelist)
                role3 = discord.utils.find(lambda role: role.name == 'Streamer', rolelist)
                if 'dev' in desrole:
                    if role2 in message.author.roles:
                        yield from client.remove_roles(message.author, role2)
                        yield from client.send_message(message.channel, str(self.botmessages['remove_command_data'][0]))
                    else:
                        yield from client.send_message(message.channel, str(self.botmessages['remove_command_data'][2]))
                elif 'stream' in desrole:
                    if role3 in message.author.roles:
                        yield from client.remove_roles(message.author, role3)
                        yield from client.send_message(message.channel, str(self.botmessages['remove_command_data'][1]))
                    else:
                        yield from client.send_message(message.channel, str(self.botmessages['remove_command_data'][3]))
            else:
                return

    @asyncio.coroutine
    def bot_say_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + 'say'):
            if message.author.id in self.banlist['Users']:
                return
            else:
                say = message.content[len(self._bot_prefix + "say "):].strip()
                if say.rfind(self._bot_prefix) != -1:
                    message_data = str(self.botmessages['say_command_data'][0]).format(message.author)
                    yield from client.send_message(message.channel, message_data)
                elif say.rfind("@") != -1:
                    message_data = str(self.botmessages['say_command_data'][1]).format(message.author)
                    yield from client.send_message(message.channel, message_data)
                else:
                    try:
                        yield from client.send_message(message.channel, say)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
                    except discord.errors.HTTPException:
                        return

    @asyncio.coroutine
    def more_commands_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if client.user.mention in message.content:
            yield from self.bot_mentioned_helper(client, message)
        elif message.content.startswith(self._bot_prefix + "clear"):
            if message.author.id in self.banlist['Users']:
                return
            else:
                yield from self.clear_command_iterater_helper(client, message)
        elif message.content.startswith(self._bot_prefix + 'botban'):
            if message.author.id == self.owner_id:
                if len(message.mentions) < 1:
                    try:
                        yield from client.send_message(message.channel, str(
                            self.botmessages['bot_ban_command_data'][2]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
                else:
                    if message.mentions[0].id not in self.banlist['Users']:
                        try:
                            self.banlist['Users'].append(message.mentions[0].id)
                            json.dump(self.banlist, open("{0}{1}resources{1}ConfigData{1}BotBanned.json".format(
                                self.path, self.sepa), "w"))
                            try:
                                message_data = str(
                                    self.botmessages['bot_ban_command_data'][0]).format(message.mentions[0])
                                yield from client.send_message(message.channel, message_data)
                            except discord.errors.Forbidden:
                                yield from BotPMError.resolve_send_message_error(client, message)
                            except Exception as e:
                                str(e)
                                try:
                                    messagedata = str(
                                        self.botmessages['bot_ban_command_data'][1]).format(message.mentions[0])
                                    message_data = messagedata + str(self.botmessages['bot_ban_command_data'][2])
                                    yield from client.send_message(message.channel, message_data)
                                except discord.errors.Forbidden:
                                    yield from BotPMError.resolve_send_message_error(client, message)
                        except discord.errors.Forbidden:
                            yield from BotPMError.resolve_send_message_error(client, message)
        elif message.content.startswith(self._bot_prefix + 'botunban'):
            if message.author.id == self.owner_id:
                if len(message.mentions) < 1:
                    try:
                        yield from client.send_message(message.channel, str(
                            self.botmessages['bot_unban_command_data'][2]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
                else:
                    if message.mentions[0].id in self.banlist['Users']:
                        try:
                            tobotunban = self.banlist['Users']
                            tobotunban.remove(message.mentions[0].id)
                            json.dump(self.banlist, open("{0}{1}resources{1}ConfigData{1}BotBanned.json".format(
                                self.path, self.sepa), "w"))
                            try:
                                message_data = str(
                                    self.botmessages['bot_unban_command_data'][0]).format(message.mentions[0])
                                yield from client.send_message(message.channel, message_data)
                            except discord.errors.Forbidden:
                                yield from BotPMError.resolve_send_message_error(client, message)
                        except Exception as e:
                            str(e)
                            try:
                                messagedata = str(
                                    self.botmessages['bot_unban_command_data'][1]).format(message.mentions[0])
                                message_data = messagedata + str(self.botmessages['bot_unban_command_data'][2])
                                yield from client.send_message(message.channel, message_data)
                            except discord.errors.Forbidden:
                                yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def userdata_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if message.content.startswith(self._bot_prefix + "userinfo"):
            if message.author.id in self.banlist['Users']:
                return
            else:
                for disuser in message.mentions:
                    username = disuser.name
                    seenin = set(
                        [member.server.name for member in client.get_all_members() if member.name == username])
                    seenin = str(len(seenin))
                    if str(disuser.game) != 'None':
                        desuser = disuser
                        msgdata_1 = str(self.botmessages['userinfo_command_data'][0]).format(desuser, seenin)
                        message_data = msgdata_1
                        data = message_data
                    else:
                        desuser = disuser
                        msgdata_1 = str(self.botmessages['userinfo_command_data'][0]).format(desuser, seenin)
                        message_data = msgdata_1.replace("Playing ", "")
                        data = message_data
                    try:
                        yield from client.send_message(message.channel, data)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
                    break
                else:
                    seenin = set(
                        [member.server.name for member in client.get_all_members()
                         if member.name == message.author.name])
                    seenin = str(len(seenin))
                    if str(message.author.game) != 'None':
                        msgdata_1 = str(self.botmessages['userinfo_command_data'][0]).format(message.author, seenin)
                        message_data = msgdata_1
                        data = message_data
                    else:
                        msgdata_1 = str(self.botmessages['userinfo_command_data'][0]).format(message.author, seenin)
                        message_data = msgdata_1.replace("Playing ", "")
                        data = message_data
                    try:
                        yield from client.send_message(message.channel, data)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def convert_url_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        # This command has been optimized for TinyURL3 0.1.5
        if message.content.startswith(self._bot_prefix + 'tinyurl'):
            if self.disabletinyurl:
                return
            else:
                url = message.content[len(self._bot_prefix + "tinyurl "):].strip()
                if '<' and '>' in url:
                    url = url.strip('<')
                    url = url.strip('>')
                try:
                    self.link = TinyURL.create_one(url)
                    self.tinyurlerror = False
                except TinyURL.errors.URLError:
                    self.tinyurlerror = True
                    try:
                        yield from client.send_message(message.channel, str(
                            self.botmessages['tinyurl_command_data'][2]))
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
                except TinyURL.errors.InvalidURL:
                    self.tinyurlerror = True
                    try:
                        result = str(self.botmessages['tinyurl_command_data'][1])
                        yield from client.send_message(message.channel, result)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)
                if not self.tinyurlerror:
                    self.link = str(self.link)
                    result = str(self.botmessages['tinyurl_command_data'][0]).format(self.link)
                    try:
                        yield from client.send_message(message.channel, result)
                    except discord.errors.Forbidden:
                        yield from BotPMError.resolve_send_message_error(client, message)

    @asyncio.coroutine
    def scan_for_invite_url_only_pm_code(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        if self._is_official_bot:
            if message.content.startswith('https://discord.gg/'):
                yield from client.send_message(message.channel, str(self.botmessages['join_command_data'][3]))
            if message.content.startswith('http://discord.gg/'):
                yield from client.send_message(message.channel, str(self.botmessages['join_command_data'][3]))


class BotCommands:
    """
    Basic Messge Commands.
    """
    def __init__(self):
        self.bot = BotData()

    @asyncio.coroutine
    def attack(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.attack_code(client, message)

    @asyncio.coroutine
    def randomcoin(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.randomcoin_code(client, message)

    @asyncio.coroutine
    def colors(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.colors_code(client, message)

    @asyncio.coroutine
    def debug(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.debug_code(client, message)

    @asyncio.coroutine
    def games(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.games_code(client, message)

    @asyncio.coroutine
    def invite(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.invite_code(client, message)

    @asyncio.coroutine
    def kills(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.kills_code(client, message)

    @asyncio.coroutine
    def mod_commands(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.mod_commands_code(client, message)

    @asyncio.coroutine
    def other_commands(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.other_commands_code(client, message)

    @asyncio.coroutine
    def prune(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.prune_code(client, message)

    @asyncio.coroutine
    def bot_roles(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.bot_roles_code(client, message)

    @asyncio.coroutine
    def bot_say(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.bot_say_code(client, message)

    @asyncio.coroutine
    def more_commands(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.more_commands_code(client, message)

    @asyncio.coroutine
    def userdata(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.userdata_code(client, message)

    @asyncio.coroutine
    def convert_url(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.convert_url_code(client, message)

    @asyncio.coroutine
    def scan_for_invite_url_only_pm(self, client, message):
        """
        Bot Commands.
        :param client: Discord Client.
        :param message: Messages.
        :return: Nothing.
        """
        yield from self.bot.scan_for_invite_url_only_pm_code(client, message)
