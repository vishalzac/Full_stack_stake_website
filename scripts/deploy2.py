import pstats


from brownie import DappToken
from scripts.helpful_scripts import get_account


def deploy():
    account = get_account()
    dep = DappToken.deploy({"from": account})

    print(dep)


def main():
    deploy()
