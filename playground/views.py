# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .processor import domain_check_parallel
from .serializers import DomainSerializer

# domains = [
#     "https://www.ixfi.com/",
#     "https://rewards.ixfi.com/task-center/milestone-all",
#     "https://www.ixfi.com/help-center/buy-crypto/how-to-purchase-crypto-using-a-credit-or-debit-card-through-simplex",
#     "https://www.ixfi.com/trade/ETH/USDT",
#     "https://www.ixfi.com/help-center/referral-affiliate/how-to-redeem-ixfi-points",
#     "https://www.ixfi.com/static-pages/page/terms",
#     "https://www.ixfi.com/market",
#     "https://www.ixfi.com/page/cookies-policy",
#     "https://www.ixfi.com/help-center/buy-crypto/how-to-purchase-crypto-using-a-credit-or-debit-card-through-transak",
#     "https://www.ixfi.com/auth/register",
#     "https://www.ixfi.com/static-pages/contact-us",
#     "https://www.ixfi.com/help-center/referral-affiliate/how-to-earn-ixfi-points-through-task-centre",
#     "https://www.ixfi.com/wallet/deposit/USDT",
#     "https://www.ixfi.com/help-center/buy-crypto",
#     "https://research.ixfi.com/news",
#     "https://www.ixfi.com/help-center/account-activities",
#     "https://rewards.ixfi.com/",
#     "https://www.ixfi.com/go/app/",
#     "https://www.ixfi.com/contact-us",
#     "https://rewards.ixfi.com/task-center/milestone-all",
#     "https://www.ixfi.com/static-pages/referral-landing",
#     "https://rewards.ixfi.com/task-center/one-time-all",
#     "https://www.ixfi.com/manifesto",
#     "https://www.ixfi.com/static-pages/news",
#     "https://www.ixfi.com/go/team/",
#     "https://www.ixfi.com/trade/BTC/USDT",
#     "https://www.ixfi.com/blog/",
#     "https://www.ixfi.com/page/terms",
#     "https://www.ixfi.com/help-center/security",
#     "https://www.ixfi.com/static-pages/page/privacy_policy",
#     "https://www.ixfi.com/help-center/swap-convert",
#     "https://www.ixfi.com/trade",
#     "https://www.ixfi.com/help-center/referral-rewards",
#     "https://www.ixfi.com/swap",
#     "https://www.ixfi.com/static-pages/page/cookies-policy",
#     "https://www.ixfi.com/",
#     "https://www.ixfi.com/help-center/referral-affiliate/referral-guide",
#     "https://www.ixfi.com/help-center",
#     "https://www.ixfi.com/fee-structure",
#     "https://www.ixfi.com/help-center/coin-info",
#     "https://www.ixfi.com/market/list/spot",
#     "https://rewards.ixfi.com/task-center/monthly-all",
#     "https://www.ixfi.com/market/list",
#     "https://rewards.ixfi.com/rewards",
#     "https://www.ixfi.com/auth/forget-password",
#     "https://www.ixfi.com/help-center/referral-affiliate/how-to-check-the-history-in-a-reward-program",
#     "https://www.ixfi.com/news",
#     "https://www.ixfi.com/convert",
#     "https://www.ixfi.com/home/landing",
#     "https://www.ixfi.com/page/privacy_policy",
#     "https://www.ixfi.com/help-center/wallet",
#     "https://research.ixfi.com/",
#     "https://www.ixfi.com/help-center/other-topics",
#     "https://www.ixfi.com/static-pages/manifesto",
#     "https://www.ixfi.com/help-center/signup",
#     "https://www.ixfi.com/best-buy-crypto-offers",
#     "https://rewards.ixfi.com/leaderboard"
# ]

# Create your views here.
class DomainStatus(APIView):
    def post(self, request):
        domains = request.data.get("domains", [])
        results = domain_check_parallel(domains)
        serializer = DomainSerializer(results, many=True)
        return Response(serializer.data, status=200)
        