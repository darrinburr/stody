#
# copyright Aug. 2010 darrin burr
#


# stody - about fall 1969 in an opel cadette vehicle, I was 3yo. I could not say "stale"
# I could just say 'stody' - def. - stiff, rubbery, once having
# taste/flavour now tastless/non descript flavor; in reference to gum.
# usage "I have been chewing my gum for hours... my gum is stody"

import cgi
import os
import datetime
import time
import pymongo

print "import section .. complete"
#import webapp2

from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import db, webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
# from datetime import date, datetime

print "api and extensibles .. complete"

# set database/datastore this the real one


class word(db.Model):
    #   main db
    #   (encoding='utf-8')

    #      Official time stamp MAIN KEY    note: should be date_key_UTC
    date = db.DateTimeProperty(auto_now_add=True)
#      Edit date
    editdate = db.DateTimeProperty()
# WORD SECTION
#      actual word StringProperty
    word = db.StringProperty(default=None)
#      Is or Not 'a word' active/not active, rejected   identifier
    wordactive = db.StringProperty(default="Is")
#      International languages
    language = db.StringProperty(default="English")
# Noun-n. Verb-v. Pronoun-pron. Adverb-adv. Adjective-adj.
# Preposition-prep. Conjunction-conj. Interjection-interj.
    part = db.StringProperty()
#      actual definition of the word
    definition = db.StringProperty()
#      pic (optional)
    wordpiclink = db.LinkProperty()
#      supporting link (optional)
    link = db.LinkProperty()
#      derivative  (optional) 'base word(s)'  ie. "stale" is to stody
    derivative = db.StringProperty()
# how it came about (optional) origin where/why it came about.  ie. we
# were playing risk downstairs 11-04-89
    history = db.StringProperty(multiline=True)
#      example of how it's used    note: was usage
    example = db.StringProperty()
# NOT USED - (INCORPORATED INTO PART)   word, slogan/coined phrase, ect.
    wordtype = db.StringProperty(default=" ")
#      users phoenetic representation
    pronunciation = db.StringProperty(default=None)
# RATING SECTION
# NOTE: the  'adult_rating'  G, PG(general dictionary), R(f-word), RI
# [/rude/Innaproprate/racist/offensive/sexual content/adult 'live' comedy
# (not overtly sexual in nature), X (pornographic/erotic/hard core or
# sexual in content)
    adultrating = db.StringProperty()
#      users rating, users rate each others words
    rating = db.RatingProperty()
#      users rating average
    ratingaverage = db.FloatProperty(default=0.0)
#      other users that like/use this 'word'
    like = db.IntegerProperty(default=1)
#      for future use
    count = db.IntegerProperty(default=0)
# BASIC USER INFO
#      user identifier default=email but could be mac address
    useridentifier = db.StringProperty()
#      last name required by www.uspto.gov Rule 2.22(a) Item 1
    full = db.StringProperty(default='Anonymous')
#      user input or 'fb name' first/first and last/nickname/FB name
    nickname = db.StringProperty(default='Anonymous')
#      address required by www.uspto.gov Rule 2.22(a) Item 1
    address = db.StringProperty()
#      postcode
    postcode = db.StringProperty()
#      email address required by www.uspto.gov Rule 2.22(a) Item 6
    email = db.EmailProperty(default='anonymous@email.com')
#      all check boxes check permission from user to post word
    userpermissionconf = db.StringProperty(default="No")
#      all check boxes check permission from user to post word
    userpermissionconstr = db.StringProperty(default="No")
#      all check boxes check permission from user to post word
    userpermissiontm = db.StringProperty(default="No")
#      user invoice number alphanumeric
    invoice = db.StringProperty()
#      direct link to your word "quick link"
    accesslink = db.LinkProperty()


class comment(db.Model):
    #      comment db

    #      comment date
    datecomment = db.DateTimeProperty(auto_now_add=True)
#      key date from orig. word
    dateword = db.DateTimeProperty()
#      comment date
    datecomment = db.DateTimeProperty()
#      comment
    comment = db.StringProperty()
#      other users that like/use this comment
    like = db.IntegerProperty(default=1)
#      user input or 'fb name' first/first and last/nickname/FB name
    nickname = db.StringProperty(default='Anonymous')
#      email of commenter
    email = db.EmailProperty(default='anonymous@email.com')


status = "Your Word not Found"


class msg(db.Model):

    #      date of status creation
    date = db.DateTimeProperty(auto_now_add=True)
#      state of status
    statustype = db.StringProperty(default="None")
#      status
    status = db.StringProperty(default="your werd not found")
#      state of status
    statestatus = db.StringProperty(default="Not Active")


#######
#
# HTML Pages Section
#
#######

    #######
    #
    # Resume Section
    #
    #######

# SHERRY STEED
class SherryCover(webapp.RequestHandler):
    def get(self):
        template_file_name = 'sherry_cover.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class SherryResume(webapp.RequestHandler):
    def get(self):
        template_file_name = 'sherry_resume.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class SherryReferences(webapp.RequestHandler):
    def get(self):
        template_file_name = 'sherry_references.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))

# DARRIN BURR


class DarrinCover(webapp.RequestHandler):
    def get(self):
        template_file_name = 'darrin_cover.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class DarrinResume(webapp.RequestHandler):
    def get(self):
        template_file_name = 'darrin_resume.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class DarrinReferences(webapp.RequestHandler):
    def get(self):
        template_file_name = 'darrin_references.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class MainPage(webapp.RequestHandler):
    def get(self):
        template_file_name = 'index.html'
        # worlds newest word!!!

        newestword = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R', 'RI') AND wordactive = 'Is' ORDER BY date DESC LIMIT 1")

        # next line works gr8 been in use for months!!!
        #newestword = word.all().order('-date').fetch(1)

        # Example code
        #greetings_query = Greeting.all().order('-date')
        #greetings = greetings_query.fetch(10)

        #status = db.GqlQuery("SELECT * FROM msg WHERE msg = :title", title="hold")
        #status = msg.status('hold')
#myCar = Cars(make="Ford", year=2009)

        #status = msg.status.asc('-status').fetch(1)

        #status = db.GqlQuery("SELECT * FROM msg WHERE status = 'STOP' ").fetch(20)
        #"ORDER BY when DESC").fetch(1)

        # next 3 lines work..  :)
        #msgset = msg.all().order('-status')
        #msgset.status = 'Found'
        #status = msgset.status

        template_values = {
            'recordnewest': newestword,  # "the newest" word (set)
            # 'records': newestword,
            'status': status,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewPage(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view.html'
        # order by date
        records = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R') AND wordactive = 'Is' AND userpermissionconf = 'Yes' AND userpermissionconstr = 'Yes' AND userpermissiontm = 'Yes' ORDER BY word DESC")
        #records = word.all().order('-date').fetch(100)
        #userid = word.get_by_id()
        #query = word.all().word.sort()

        #query.filter('title =', 'Foo')

        #recordsort = records.sort()
        #records = word(word='jombie')

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewAlpha(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view_alpha.html'
        # order by alphabetic
        records = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R', 'RI') AND wordactive = 'Is' AND userpermissionconf = 'Yes' AND userpermissionconstr = 'Yes' AND userpermissiontm = 'Yes' ORDER BY date DESC")

        # WHERE name IN ('Bob', 'Jane') AND age != 25"

        #records = word.all().order('word')

        #query = word.all()

        #records = word.gql("ORDER BY word")

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewDateNewest(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view_date_newest.html'
        # order by date
        records = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R') AND wordactive = 'Is' AND userpermissionconf = 'Yes' AND userpermissionconstr = 'Yes' ORDER BY date DESC")
        #records = word.all().order('-date').fetch(100)

        #query = word.all()

        # date should be pre-formated before being sent ie.  "Today is: {0:a b
        # d H:M:S Y}".format(datetime.now())

        # HUMM!!!!!!??? works but nothin'
        # for result in records:
        #word = {}
        #date = format({'0:a b d H:M:S Y': result.date})
        #date = {'0:a b d H:M:S Y'}.format(records.date)

        #movie['title'] = result.title
        ##movie['summary'] = result.summary
        #movie['release_date'] = result.release_date.ctime()
        #movie['pic'] = 'image?' + urllib.urlencode({'title': result.title})

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewToday(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view_today.html'
        # order by date

        # these next 2 lines ARE AWESOME!!!
        # these get date today and the current date/time right now!!
        todayonly = datetime.date.today()
        now = datetime.datetime.now()
        # yesterdaysdate = datetime.datetime.now() #- datetime.timedelta(days =
        # 3)

        # next 2 lines work gr8 for display but not in a GQL query ie. for
        # format only
        todaysdate = time.strftime("%m-%d-%Y", time.localtime(time.time()))
        othertodaysdate = time.strftime(
            "%Y-%d-%m", time.localtime(time.time()))

        #  Example code -broke- start_time = '%s.000Z' % datetime.datetime.strptime('%d/%m/%Y %H:%M').isoformat()
        # Example code -broke-
        # time=datetime.datetime.strptime(self.request.get('datetimestamp'),
        # '%d/%m/%Y %H:%M')

        #records = word.all().where( date = todayonly).order('-date')
        #days.filter("d_date >=", start_date)

        # these 2 lines works!!
        #query = word.all()
        #records = query.order('date')

        # i beleive this next line dose not work because its comparing a str not date format
        #records = db.GqlQuery("SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R') AND date = :1 ", '2010-11-10 23:55:00.624879')

        records = db.GqlQuery(
            "SELECT * FROM word WHERE date > :1 AND adultrating IN ('G', 'PG', 'R', 'RI') AND wordactive = 'Is' AND userpermissionconf = 'Yes' AND userpermissionconstr = 'Yes'", todayonly)

        #users = db.Query(UserInformation).filter("login_date >", three_days_ago).fetch(10)

        #Schedule.all().filter("station =", foo.key())
        #query = recordsd
        #tax = query.filter('active =', 'Not')

        #query = records
        #query.filter('date =', today)

        template_values = {
            'records': records,  # whole set for "today"
            'today': todayonly,  # one variable
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewRated(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view_rated.html'
        # order by date

        # get todayonly = date

        records = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R') AND wordactive = 'Is' AND userpermissionconf = 'Yes' AND userpermissionconstr = 'Yes' AND userpermissiontm = 'Yes' ORDER BY like DESC")
        #records = word.all().where( date = todayonly).order('-date')

        # these 2 lines works!!
        #query = word.all()
        #records = query.order('date')

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewFull(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view_full.html'
        # order by alphabetic

        records = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R', 'RI', 'X') AND wordactive = 'Is' ORDER BY date DESC")
        #records = word.all().order('word')

        #query = word.all()

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewAcro(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view_acro.html'
        # order by alphabetic

        records = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R') AND wordactive = 'Is' AND userpermissionconf = 'Yes' AND userpermissionconstr = 'Yes' AND userpermissiontm = 'No' AND part = 'Acronym' ORDER BY date DESC")
        #records = word.all().order('word')

        #query = word.all()

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewTM(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view_tm.html'
        # order by alphabetic
        records = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R', 'RI') AND wordactive = 'Is' AND userpermissionconf = 'Yes' AND userpermissionconstr = 'Yes' AND userpermissiontm = 'Yes' ORDER BY date DESC")

        # WHERE name IN ('Bob', 'Jane') AND age != 25"

        #records = word.all().order('word')

        #query = word.all()

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewTop10(webapp.RequestHandler):
    def get(self):
        # It's actually TOP 3, but could be TOP 10!!!!!!!!!!!!
        template_file_name = 'view_top10.html'
        # order by date

        # get todayonly = date

        records = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('G', 'PG', 'R', 'RI', 'X') AND wordactive = 'Is' ORDER BY like DESC LIMIT 3")
        #records = word.all().where( date = todayonly).order('-date')

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class ViewX(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view_x.html'
        # order by date

        records = db.GqlQuery(
            "SELECT * FROM word WHERE adultrating IN ('R', 'RI', 'X') AND wordactive = 'Is' ORDER BY word DESC")
        #records = word.all().where( date = todayonly).order('-date')

        #records = word.all()
        #records.filter('adultrating =', 'G').filter('adultrating =', 'RI')
        ##records.filter('adultrating =', 'R')
        # records.order("-word")

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class AddWord(webapp.RequestHandler):
    def get(self):
        template_file_name = 'addword.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class About(webapp.RequestHandler):
    def get(self):
        template_file_name = 'about.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class AboutQA(webapp.RequestHandler):
    def get(self):
        template_file_name = 'about_qa.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class AboutExec(webapp.RequestHandler):
    def get(self):
        template_file_name = 'about_exec.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class AboutTimeline(webapp.RequestHandler):
    def get(self):
        template_file_name = 'about_timeline.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class AboutTech(webapp.RequestHandler):
    def get(self):
        template_file_name = 'about_tech.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class AboutPress(webapp.RequestHandler):
    def get(self):
        template_file_name = 'about_press.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class AboutPP(webapp.RequestHandler):
    def get(self):
        template_file_name = 'about_pp.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class AboutTOS(webapp.RequestHandler):
    def get(self):
        template_file_name = 'about_tos.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


class Contact(webapp.RequestHandler):
    def get(self):
        template_file_name = 'contact.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


# class AboutTech(webapp.RequestHandler):
#    def get(self):
#        template_file_name = 'about_tech.html'
#
#
# no template values needed... just rendering text
#        template_values = {
#
#           }
#
#        path = os.path.join(os.path.dirname(__file__), template_file_name)
#        self.response.out.write(template.render(path, template_values))


######
# this routine was to handles all text ONLY html pages (no values) but didn't work  meehh
#####
class TextPage(webapp.RequestHandler):
    def post(self):

        # web page sends requested page as a value passed in from form on html
        # page
        callpage = self.request.get('page')
        # .html added to the request
        template_file_name = callpage + ".html"

        # no template values needed... just rendering text

        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))

        # self.redirect(callpage)


class SearchQuick(webapp.RequestHandler):
    def get(self):
        template_file_name = 'about.html'
        #template_file_name = 'html_right_column.html'

        #records = word.all().order('-date').fetch(1)
        #greetingsquery = Greeting.all().order('-date')
#        status = word.all().word(status).fetch(1)

#        if status:
#            status = status
#        else:
#            status = status

#           if word.word =
# self.response.out.write('<b color=blue>%s</b> wrote:' %
# greeting.author.nickname()

        # someone has your word :(
#            search_message = 'sorry someone has your word'

#        else:
        # your word dose not exist :) reg. it!!!
        status = "please wait..."
        #status = unicode(self.request.get('word'))

        template_values = {
            #'records': records,
            'status': status,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))

#######
# Database Subroutines Section
#######

# this is the "post-to-database" from the addword page 'on submit'


class Record(webapp.RequestHandler):
    def post(self):
        record = word()

        # Word Section
        record.language = self.request.get('language')
        record.word = unicode(self.request.get('word'))
        # NOT USED - record.word_type = self.request.get('word_type')
        record.part = self.request.get('part')
        record.pronunciation = unicode(self.request.get('pronunciation'))
        record.definition = unicode(self.request.get('definition'))
        #record.wordpiclink = unicode(self.request.get('wordpiclink'))
        record.example = unicode(self.request.get('example'))
        #record.link = unicode(self.request.get('link'))
        record.history = unicode(self.request.get('history'))
        record.adultrating = self.request.get('adultrating')

        # Basic Info Section
        record.full = unicode(self.request.get('full'))
        record.nickname = unicode(self.request.get('nickname'))
        record.email = unicode(self.request.get('email'))
        record.address = unicode(self.request.get('address'))
        record.postcode = unicode(self.request.get('postcode'))

        # Check box Section
        record.userpermissionconf = unicode(
            self.request.get('userpermissionconf'))
        record.userpermissionconstr = unicode(
            self.request.get('userpermissionconstr'))
        record.userpermissiontm = unicode(self.request.get('userpermissiontm'))


# problem with next line in GAE  int something
#...........main.py", line 193, in post
#    record.like = int(self.request.get('like'))
# ValueError: invalid literal for int() with base 10: ''

#        record.like = int(self.request.get('like'))
#        record.ratingaverage = self.request.get('ratingaverage')

        record.put()
#       self.redirect('/') = Index.html
        self.redirect('/')


# this section is for the search button
class SearchDictionarys(webapp.RequestHandler):
    def post(self):
        msgset = msg()

        searhthis = self.request.get('check')

        # make search this all lc

        #records = db.GqlQuery("SELECT * FROM word WHERE word = :1 ", searhthis)

        # these 2 lines works!!
        #query = word.all()
        #records = query.order('date')

        query = word.Query('word')
        query['word ='] = searhthis
        records = query.Get(1)
        if len(records) < 1:
            status = 'word not fownd'
        else:
            status = 'fownd!'

        # these 2 lines work! they put the searched word in the msg db
        #msgset.status = self.request.get('check')
        # msgset.put()

        # next 3 lines work..  :)
        #msgset = msg.all().order('-status')
        #msgset.status = 'Found'

        #status = msgset.status

        # self.redirect('/html_right_column')
        self.redirect('/search_results')


class GetDefinition(webapp.RequestHandler):
    def get(self):
        template_file_name = 'view_date_newest.html'
        # web page sends word to get definition for.. as a value passed in from
        # form on html page
        getdefinitiondb = self.request.get('get_definition_db')

        #records = db.GqlQuery("SELECT * FROM word WHERE word = getdefinitiondb ORDER BY word DESC")
        #records = word.all().where( date = todayonly).order('-date')

        records = word.all().filter('word =', getdefinitiondb).fetch(1)
        #records.filter('word =', getdefinitiondb)
        ##records.filter('adultrating =', 'R')
        # records.order("-word")
        # records.fetch(1)

# these 2 line works!!
        #query = word.all()
        #records = query.order('date')

        #records = word.gql("ORDER BY word")

        template_values = {
            'records': records,
        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


# PHP test section
class TestPage(webapp.RequestHandler):
    def post(self):

        self.redirect('/testpage')

# CG&O section


class CgoPage(webapp.RequestHandler):
    def get(self):
        template_file_name = 'cgo_index.html'


# no template values needed... just rendering text
        template_values = {

        }

        path = os.path.join(os.path.dirname(__file__), template_file_name)
        self.response.out.write(template.render(path, template_values))


apps_binding = []

apps_binding.append(('/darrin_cover', DarrinCover))
apps_binding.append(('/darrin_resume', DarrinResume))
apps_binding.append(('/darrin_references', DarrinReferences))
apps_binding.append(('/sherry_cover', SherryCover))
apps_binding.append(('/sherry_resume', SherryResume))
apps_binding.append(('/sherry_references', SherryReferences))
apps_binding.append(('/', MainPage))
apps_binding.append(('/html_right_column', SearchQuick))
apps_binding.append(('/view', ViewPage))
apps_binding.append(('/view_date_newest', ViewDateNewest))
apps_binding.append(('/view_alpha', ViewAlpha))
apps_binding.append(('/view_today', ViewToday))
apps_binding.append(('/view_rated', ViewRated))
apps_binding.append(('/view_full', ViewFull))
apps_binding.append(('/view_tm', ViewTM))
apps_binding.append(('/view_acro', ViewAcro))
apps_binding.append(('/view_top10', ViewTop10))
apps_binding.append(('/view_x', ViewX))
apps_binding.append(('/addword', AddWord))
apps_binding.append(('/about', About))
apps_binding.append(('/about_qa', AboutQA))
apps_binding.append(('/about_exec', AboutExec))
apps_binding.append(('/about_timeline', AboutTimeline))
apps_binding.append(('/about_tech', AboutTech))
apps_binding.append(('/about_press', AboutPress))
apps_binding.append(('/about_pp', AboutPP))
apps_binding.append(('/about_tos', AboutTOS))
apps_binding.append(('/contact', Contact))
apps_binding.append(('/new', Record))
apps_binding.append(('/get_definition', GetDefinition))
apps_binding.append(('/searchquick', SearchDictionarys))
apps_binding.append(('/shane', TestPage))
apps_binding.append(('/textpage', TextPage))
apps_binding.append(('/cgo_index', CgoPage))

application = webapp.WSGIApplication(apps_binding, debug=True)


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
