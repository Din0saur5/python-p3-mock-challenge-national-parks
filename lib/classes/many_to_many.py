
from datetime import datetime

class NationalPark:    
#all for most visited bonus fn
    all= []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
        
# validate name input        
    @property
    def name(self):
        return self._name    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>=3 and not hasattr(self,'name'):
            self._name = name
        else:
            raise Exception('name must be str and btw 1-15 char')
    

# returns all trips at a park using list comp 
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]
#returns a unique list of visitors at a park using a set and list comp and all class var   
    def visitors(self):
        return list({trip.visitor for trip in Trip.all if trip.national_park is self})
#uses previous trips fn to determine number of visits    
    def total_visits(self):
        return len(self.trips())
# uses lambda fn and sorted to return the visitor who has been the most using their fn
    def best_visitor(self):
        best = sorted(self.visitors(), key=lambda n: n.total_visits_at_park(park=self), reverse = True)
        return best[0] if len(best) >0 else None
    
    @classmethod
    def most_visited(cls):
        best = sorted(cls.all, key=lambda n: n.total_visits(), reverse = True)
        return best[0] if len(best) >0 else None
   
            

class Trip:
    
    all =[]
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

#validates startdate input using standard methods and datetime import for date format 
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
# using datetime (import) is strict about format have to parse the ordinal number suffix out and for st to avoid messing up august have to specify the 1st for 1st, 21st, and 31st
        start_date_parsed = start_date.replace('1st', '1').replace('nd', '').replace('rd', '').replace('th', '')
#capital %B for full month and %b for month abrv %d for day
        if isinstance(start_date, str) and len(start_date)>=7 and datetime.strptime(start_date_parsed, "%B %d") :     
            self._start_date = start_date
        else:
            raise Exception('start_date must be str and btw >=7 char and in "Month day format"')

#same code as state_date jsut with end_date   
    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):

        end_date_parsed = end_date.replace('1st', '1').replace('nd', '').replace('rd', '').replace('th', '')

        if isinstance(end_date, str) and len(end_date)>=7 and datetime.strptime(end_date_parsed, "%B %d") :
             
            self._end_date = end_date
        else:
            raise Exception('end_date must be str and btw >=7 char and in "Month day format"')    

#validate Visitor input 
    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self,visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception('Not a visitor')
        
#validate Park input 
    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self,national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception('Not a National Park')
   
   
        
class Visitor:

    def __init__(self, name):
        self.name = name

# validate name input        
    @property
    def name(self):
        return self._name    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>0 and  len(name) <16:
            self._name = name
        else:
            raise Exception('name must be str and btw 1-15 char')

# standard list comp to get all trips for visitor      
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
# same list comp and set magic as before    
    def national_parks(self):
        return list({trip.national_park for trip in Trip.all if trip.visitor is self})
    
# good filter fn to use in prev fn     
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park is park])