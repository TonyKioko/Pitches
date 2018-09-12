import unittest
from app.models import Pitches, User,Comments
from app import db



class PitchesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitches class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_user = User(username = 'Tony', password = 'potato', email = 't@g.com')
        self.new_comment = Comments(the_comment = 'New Comment', pitches_id = 1, user_id=self.new_user)
        self.new_pitch = Pitches(id=1,body="New Pitch",category='Promotion-Pitch',published=10/9/18,user_id = 1,comments = self.new_comment)

    def tearDown(self):
        db.session.delete(self)
        # User.query.delete()
        Pitches.query.delete()
    
    def test_instance(self):
        '''
        Test case to check if new_comment is an instance of Comment
        '''

        self.assertTrue( isinstance( self.new_comment, Comments) )
        self.assertTrue( isinstance( self.new_user, User) )
        self.assertTrue( isinstance( self.new_pitch, Pitches) )
    

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,1)
        self.assertEquals(self.new_pitch.body,'New Pitch')
        self.assertEquals(self.new_pitch.category,"Promotion-Pitch")
        self.assertEquals(self.new_pitch.publshed,10/9/18)
        self.assertEquals(self.new_pitch.user_id,1)
        self.assertEquals(self.new_pitch.comments,self.new_comment)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        # db.session.commit()
        self.assertTrue(len(Pitches.query.all())>0)

    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        pitches = Pitches.get_pitches(1)
        self.assertTrue(len(pitches) == 1)

class TestComment(unittest.TestCase):
	
	def setUp(self):
		self.comment = Comments(the_comment="new comment",user_id=1,pitches_id=1)

	def tearDown(self):
		
		Comments.query.delete()

	def test_check_comment_instance_variables(self):
		
		self.assertEquals(self.comment.the_comment,"new comment")
		self.assertEquals(self.comment.user_id, 1)
    
