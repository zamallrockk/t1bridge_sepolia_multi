from colorama import Fore, Style

def show_banner():
    banner = f"""
{Fore.LIGHTRED_EX}{Style.BRIGHT}
   ███████╗ █████╗ ███╗   ███╗ █████╗ ██╗     ██╗      ██████╗ ██████╗  ██████╗██╗  ██╗
   ╚══███╔╝██╔══██╗████╗ ████║██╔══██╗██║     ██║     ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝
     ███╔╝ ███████║██╔████╔██║███████║██║     ██║     ██████╔╝██║   ██║██║     █████╔╝ 
    ███╔╝  ██╔══██║██║╚██╔╝██║██╔══██║██║     ██║     ██╔═██╗ ██║   ██║██║     ██╔═██╗ 
   ███████╗██║  ██║██║ ╚═╝ ██║██║  ██║███████╗███████╗██║  ██║╚██████╔╝╚██████╗██║  ██║
   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
{Fore.LIGHTCYAN_EX}
           Auto deposit bot to T1 Protocol bridge – by zamallrock
{Style.RESET_ALL}
"""
    print(banner)
