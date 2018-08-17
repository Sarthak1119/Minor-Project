# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 23:49:37 2018

@author: Rishabh
"""

import scrapy 

class Electrician(scrapy.Spider):
    name = "elec"
    start_urls = ["https://www.justdial.com/Alwar/Electricians/nct-10184166"]
    
    def parse(self, response):
        for href in response.xpath('//li[@class="cntanr"]/@data-href'):
            yield response.follow(href,self.getdetails)
        
        for href in response.xpath('//div[@class="jpag"]/a/@href'):
            yield response.follow(href,self.parse)
            
    def getdetails(self,response):
        
        yield{
                'Name':response.xpath('//*[@id="setbackfix"]/div[1]/div/div[1]/div[2]/div/div/h1/span/span/text()').extract_first(),
                'address':(response.xpath('//*[@id="setbackfix"]/div[1]/div/div[1]/div[2]/div/ul/li[1]/span[2]/span/span/text()').extract_first()).strip()
                }
        
        