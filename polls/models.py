"""Import the models module.
"""
from django.db import models

# Create your models here.
# use Django's built-in object-relational mapping (ORM) & define the relevant classes
# -each entry in a SQL table represents a single object, this can be converted to a class instance in Python.  
# create a question class that inherits from django.db.models.Model
class Question(models.Model):
    """The question class inherits from django.db.models.Model.
    It sets up the question model in the database table.

    :param question_text: Store the actual text of the question.
    :type question_text: str    

    :param pub_date: Store the date and time when the question was published.
    :type pub_date: datetime.datetime    
    """
    # set 2 variables that represent 2 fields in the database
    # the instance of Field class CharField tells django the type of data the question holds
    # - CharField requires a max_length (used not only in the database schema but also in validation)
    # the instance of Field class DateTimeField tells django the type of data the publication date holds
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # define a __str__ method & return question_text
    def __str__(self):
        """Return the question text.

        :return: The question text.
        :rtype: str
        """
        return self.question_text

# create a choice class that inherits from django.db.models.Model
class Choice(models.Model):
    """The class represents a choice for a question.
    It sets up the choice model in the database table.

    :param question: The foreign key to the related question.
    :type question: Question

    :param choice_text: The text of the choice.
    :type choice_text: str

    :param votes: The number of votes for the choice.
    :type votes: int
    """
    # use database foreign keys to indicate relationships between question and choices
    # - a ForeignKey field to show this many-to-one relationship
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    
    # A Field can also have various optional arguments; in this case, set the default value of votes to 0.
    votes = models.IntegerField(default=0)

    # define a __str__ method & return choice_text
    def __str__(self):
        """Return the choice text.

        :return: The text of the choice.
        :rtype: str
        """
        return self.choice_text
