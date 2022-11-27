from dataclasses import dataclass



@dataclass
class News:
    name:str
    src:str
    url:str
    attr_key:str = None
    selector:str = None
    prefix:str = None
    class_key:str = None
    
@dataclass
class Mail:
    box:str
    sender:str
   
    


class FeedFlowwings:
    @staticmethod
    def get_rss_urls():
        yield from [News(name='중국_소식', src='googleAlert', url='https://www.google.co.kr/alerts/feeds/11305193269230284098/15091211705036215232'),
                    News(name='중동_소식', src='googleAlert', url='https://www.google.co.kr/alerts/feeds/11305193269230284098/10207016080645967575'),
                    # News(name='다모다란 교수', src='rss', url='https://aswathdamodaran.blogspot.com/feeds/posts/default'),
                    # News(name='GDP NOW', src='rss', url='https://www.atlantafed.org/rss/GDPNow'),
                    News(name='EIA_today_energy', src='rss', url='https://www.eia.gov/rss/todayinenergy.xml'),
                    News(name='EIA_thisweek_petroleum', src='rss', url='https://www.eia.gov/petroleum/weekly/includes/week_in_petroleum_rss.xml')
                    ]

    @staticmethod
    def get_news_urls():
        yield from [News(name='한경_글로벌마켓', src='web', url = 'https://www.hankyung.com/globalmarket/news/hot-stock', attr_key='list_top_thumb'),
                    News(name='한경_월스리트_나우',src='web', url='https://www.hankyung.com/globalmarket/news/wallstreet-now', attr_key='list_thumb_rowtype'),
                    News(name='한경_경제', src='web', url = 'https://www.hankyung.com/economy', attr_key='main-headline'),
                    News(name='한경_금융', src='web',url = 'https://www.hankyung.com/financial-market', attr_key='main-headline'),
                    # News(name='한경 집코노미 탑기사', src='web', url = 'https://www.hankyung.com/realestate', attr_key='main-headline'),
                    # News(name='한경 집코노미 주요 기사', src='web', url = 'https://www.hankyung.com/realestate', attr_key='main-jipconomy'),
                    News(name='연포인포맥스_top', src='webWithoutHttp', url = 'https://news.einfomax.co.kr/', attr_key='auto-article auto-db02 db05', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_정책/금융', src='webWithoutHttp', url = 'https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N15&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    # News(name='연포_인포_맥스_많이_본_뉴스', src='webWithoutHttp', url = 'https://news.einfomax.co.kr/', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_채권/외환', src='webWithoutHttp',  url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N16&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_해외주식', src='webWithoutHttp', url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N21&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_글로벌경제', src='webWithoutHttp', url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N4&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/'),
                    News(name='einfomax_중국경제', src='webWithoutHttp',  url ='https://news.einfomax.co.kr/news/articleList.html?sc_section_code=S1N18&view_type=sm', attr_key='auto-article auto-db01', prefix='https://news.einfomax.co.kr/')
                    ]


    @staticmethod
    def get_mailing():
        yield from [Mail(box='WSJ', sender='WSJ Follow Alert')]
                   
   
    @staticmethod
    def get_screenNames():      
            yield from ['financialjuice',
                        'NickTimiraos']
            # 'ConsensusGurus',