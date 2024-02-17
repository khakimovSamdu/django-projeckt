from django.http import HttpResponse
# Create your views here.

def faqs(request):
    f = """Tez-tez so'raladigan savollar (FAQ, tez-tez so'raladigan savollar, tez-tez so'raladigan savollar; inglizcha tez-tez so'raladigan savollar, tez-tez so'raladigan savollar, tez-tez so'raladigan savollar; talaffuzi “ef-ey-qu”, “feck” [1]) - har qanday mavzu bo'yicha tez-tez beriladigan savollar va javoblar to'plami ular. Ushbu material formati turli Internet platformalarida mashhur.

Tez-tez so'raladigan savollar to'plami 1980-yillarning boshlarida NASA pochta ro'yxatlarining texnik cheklovlaridan kelib chiqqan Internetning matnli an'anasidir. Birinchi tez-tez so'raladigan savollar 1982 yildan boshlab Internetdan oldingi bir necha yil davomida ishlab chiqilgan. Tez-tez so'raladigan savollar qisqartmasi 1982 va 1985 yillar orasida NASA xodimi Evgeniy Miya tomonidan SPACE pochta ro'yxati uchun ishlab chiqilgan.[2][3] Keyin format boshqa pochta ro'yxatlari va Usenet yangiliklar guruhlari tomonidan qabul qilindi.

Rus tilida so'zlashuvchi muhitda inglizcha qisqartma "FAQ" tez-tez ishlatiladi. Ba'zida uning ruscha analogi mavjud - "FAQ" (bu "tez-tez so'raladigan savollar" yoki "tez-tez so'raladigan savollar va javoblar" degan ma'noni anglatishi mumkin) va "FAQ" ("tez-tez so'raladigan savollar") birinchi harflarining oddiy qisqartmasi [4]. To'g'ridan-to'g'ri transliteratsiya, FAK ("FAK-ga qarash") ham tez-tez ishlatiladi."""
    return HttpResponse(f)

def support_form(request):
    f = """There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."""
    return HttpResponse(f)
