from lxml import etree

doc = """<div class="nav_xc"><div class="nav_xc_main w760"><div class="n_fl">财政部唯一指定政府采购信息网络发布媒体 国家级政府采购专业网站</div><div class="n_fr">服务热线：400-810-1996</div></div></div>"""
html =etree.HTML(doc)

a = html.xpath(".//div[@class='nav_xc']")[0]
print(a)
print(a.xpath(".//*"))

