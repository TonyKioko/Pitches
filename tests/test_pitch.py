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

        self.user_Tony = User(username = 'Tony', password = 'potato', email = 't@g.com')
        self.new_comment = Comments(the_comment = 'New Comment', pitches_id = 1, user_id=self.user_Tony)
        self.new_pitch = Pitches(id=1,body="New Pitch",category='Promotion-Pitch',user_id = self.user_Tony,comments = self.new_comment)

    def test_instance(self):
        '''
        Test case to check if new_comment is an instance of Comment
        '''

        self.assertTrue( isinstance( self.new_comment, Comments) )

    # def test_check_instance_variables(self):
    #     self.assertEquals(self.new_pitch.id,1)
    #     self.assertEquals(self.new_pitch.body,'New Pitch')
    #     self.assertEquals(self.new_pitch.category,"Promotion-Pitch")
    #     self.assertEquals(self.new_pitch.user_id,self.user_Tony)
    #     self.assertEquals(self.new_pitch.comments,self.new_comment)

    # def test_save_pitch(self):
    #     self.new_pitch.save_pitch()
    #     self.assertTrue(len(Pitches.query.all())>0)

    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        pitches = Pitches.get_pitches(1)
        self.assertTrue(len(pitches) == 1)
    def tearDown(self):
        User.query.delete()
        Pitches.query.delete()
