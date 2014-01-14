import nuke, os
from PySide.QtGui import *
from PySide.QtCore import *
from nukescripts import panels
import jeeves_core, nukePipe

class NukeConnectGui(QWidget):
    def __init__(self, parent=None):

        #self.checkInstances()
        super(NukeConnectGui, self).__init__(parent)
        
        self.setObjectName('uk.co.thefoundry.NukeConnectGui')
 
        # Set up the window
        self.setWindowTitle('Jeeves Connect')

        self.vbox = QVBoxLayout() # main vertical sizer
        self.vbox.setContentsMargins(0,0,0,0)

        spacerItemLeft = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacerItemRight = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.default_pix = '/Users/elliott/Downloads/tmp.jpg'
        self.default_pix = os.path.join(jeeves_core.resourcesRoot, 'vfx', 'jeeves', 'icons', 'tmp.jpg')


        ################################################################################
        # JOB
        self.jobsearch = QLineEdit('', self)
        self.jobsearch.returnPressed.connect(self.findjob)
        
        self.jobsearch.setMinimumSize(QSize(245, 0))
        self.jobsearch.setMaximumSize(QSize(245, 16777215))
        
        self.jobsearchtext = QLabel('job')
        self.jobsearchbutton = QPushButton('&Find')
        self.jobsearchbutton.clicked.connect(self.findjob)
        
        self.jobsearchbutton.setMinimumSize(QSize(75, 0))
        self.jobsearchbutton.setMaximumSize(QSize(75, 100))
        
        self.hbox1_job = QHBoxLayout()
        self.hbox1_job.addItem(spacerItemLeft)
        self.hbox1_job.addWidget(self.jobsearchtext)
        self.hbox1_job.addWidget(self.jobsearch)
        self.hbox1_job.addItem(spacerItemRight)
        self.hbox1_job.addWidget(self.jobsearchbutton)

        ################################################################################
        # SHOT
        
        self.shotcombo = QComboBox(self)
        self.shotcombo.activated[str].connect(self.changeShot)
        
        self.shotcombo.setMinimumSize(QSize(245, 0))
        self.shotcombo.setMaximumSize(QSize(245, 16777215))

        self.shotcombotext = QLabel('shot')

        self.add_shot_button = QPushButton('&Add')
        self.add_shot_button.setMinimumSize(QSize(75, 0))
        self.add_shot_button.setMaximumSize(QSize(75, 100))
        
        self.add_shot_button.clicked.connect(self.addshot)
        
        self.hbox2_shot = QHBoxLayout()
        self.hbox2_shot.addItem(spacerItemLeft)
        self.hbox2_shot.addWidget(self.shotcombotext)
        self.hbox2_shot.addWidget(self.shotcombo)
        self.hbox2_shot.addItem(spacerItemRight)
        self.hbox2_shot.addWidget(self.add_shot_button)


        ################################################################################
        # THUMBNAIL

        spacer2 = QSpacerItem(90, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        spacer1 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        self.hbox3_thumb = QHBoxLayout()
        self.lbl = QLabel(self)
        self.lbl.setMinimumSize(QSize(240, 135))
        self.lbl.setPixmap(QPixmap(self.default_pix).scaled(self.lbl.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        
        self.snap = QPushButton('&Snap')
        self.snap.setMinimumSize(QSize(75, 0))
        self.snap.setMaximumSize(QSize(75, 45))
        self.snap.clicked.connect(self.snappy)
        
        
        self.hbox3_thumb.addItem(spacer1)
        self.hbox3_thumb.addWidget(self.lbl)
        self.hbox3_thumb.addItem(spacerItemRight)
        self.hbox3_thumb.addWidget(self.snap)

        ################################################################################
        # NOTES
        
        self.hbox6_notes = QHBoxLayout()
        text = ''
        #self.notes = QPlainTextEdit(text)
        self.notes = QTextEdit(text)
        self.notes.setMinimumSize(QSize(245, 135))
        self.notes.setMaximumSize(QSize(245, 135))
        
        
        self.notesnap = QPushButton('&Save')
        self.notesnap.setMinimumSize(QSize(75, 0))
        self.notesnap.setMaximumSize(QSize(75, 45))
        self.notesnap.clicked.connect(self.notesnappy)
        
        self.hbox6_notes.addItem(spacer1)
        self.hbox6_notes.addWidget(self.notes)
        self.hbox6_notes.addItem(spacerItemRight)
        self.hbox6_notes.addWidget(self.notesnap)

        ################################################################################
        # MY SCRIPTS
        
        self.scriptscombo = QComboBox(self)
        self.scriptscombo.setMinimumSize(QSize(245, 0))
        self.scriptscombo.setMaximumSize(QSize(245, 16777215))

        self.scriptscombotext = QLabel('my scripts')
        self.scriptlist = []
        list(map(self.shotcombo.addItem, []))
        self.open_my_button = QPushButton('&Open')
        self.open_my_button.setMinimumSize(QSize(75, 0))
        self.open_my_button.setMaximumSize(QSize(75, 100))
        self.open_my_button.clicked.connect(self.openmyscript)
        
        self.hbox4_myscripts = QHBoxLayout()
        self.hbox4_myscripts.addItem(spacerItemLeft)
        self.hbox4_myscripts.addWidget(self.scriptscombotext)
        self.hbox4_myscripts.addWidget(self.scriptscombo)
        self.hbox4_myscripts.addItem(spacerItemRight)
        self.hbox4_myscripts.addWidget(self.open_my_button)
        
        ################################################################################
        # ALL SCRIPTS
        
        self.allscriptscombo = QComboBox(self)
        self.allscriptscombo.setMinimumSize(QSize(245, 0))
        self.allscriptscombo.setMaximumSize(QSize(245, 16777215))


        self.allscriptscombotext = QLabel('all scripts')
        self.allscriptlist = []
        list(map(self.shotcombo.addItem, []))
        
        # open my script button
        self.allopen_my_button = QPushButton('&Open')
        self.allopen_my_button.setMinimumSize(QSize(75, 0))
        self.allopen_my_button.setMaximumSize(QSize(75, 100))
        
        self.allopen_my_button.clicked.connect(self.openallscript)
        
        self.hbox5_allscripts = QHBoxLayout()
        self.hbox5_allscripts.addItem(spacerItemLeft)
        self.hbox5_allscripts.addWidget(self.allscriptscombotext)
        self.hbox5_allscripts.addWidget(self.allscriptscombo)
        self.hbox5_allscripts.addItem(spacerItemRight)
        self.hbox5_allscripts.addWidget(self.allopen_my_button)

        ################################################################################
        # SET LAYOUT
        
        self.vbox.addLayout(self.hbox1_job)
        self.vbox.addLayout(self.hbox2_shot)
        self.vbox.addLayout(self.hbox3_thumb)
        self.vbox.addLayout(self.hbox6_notes)
        self.vbox.addLayout(self.hbox4_myscripts)
        self.vbox.addLayout(self.hbox5_allscripts)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)
    
    #################################################################################
    # GUI FUNCTIONS

    def notesnappy(self):
        print self.notes.toPlainText()


    def snappy(self):
        #lets make sure were snapping for the current shot
        shot = self.shotcombo.currentText()
        if os.getenv('SHOT') == shot:

            print 'SNAPPY'
            viewer = nuke.activeViewer()
            actInput = nuke.ViewerWindow.activeInput(viewer)
            viewNode = nuke.activeViewer().node()
            selInput = nuke.Node.input(viewNode, actInput)
            
            
            reformatPAL = nuke.nodes.Reformat( type = "to format", format = "240 135 eight_scaled", resize = 'fill') 
            reformatPAL.setInput(0, selInput) 
            
            shot_pix = '/tmp/tmp/jpg'
            shot_pix = os.path.join(jeeves_core.jobsRoot, self.job, 'vfx', 'nuke', self.shot, 'plates', 'tmp', '%s.jpg' % self.shot)
        
            
            write2 = nuke.nodes.Write( file = shot_pix, name = 'tmpWrite2' , file_type = 'jpg')
            
        
            write2.setInput(0,reformatPAL)
        
            curFrame = int(nuke.knob("frame"))
        
            nuke.execute(write2.name(), curFrame, curFrame)
        
            nuke.delete(write2)
            nuke.delete(reformatPAL)
            print 'SNAPPED'
            self.update_pix()
        else:
            print 'not snapping for current shot'

    def addshot(self):
        print 'add shot'
        #shot = nuke dialogue box - gui only, shot formatting / detection to happen in utils
        #nukePipe.jeevesConnectUtils.addshot(self.job, shot)

    def openmyscript(self):
        self.script = self.scriptscombo.currentText()
        self.openscript()

    def openallscript(self):
        self.script = self.allscriptscombo.currentText()
        if self.script:
            self.openscript()
        else:
            print 'nowt selected'
    
    def openscript(self):
        print 'OPEN SCRIPT'
        print self.job
        print self.shot
        print self.user
        print self.script
        
        if os.path.sep in self.script:
            self.fullpath = jeeves_core.searchJob.searchNukeFullpath(self.job, self.shot, '', self.script)
        else:
            self.fullpath = jeeves_core.searchJob.searchNukeFullpath(self.job, self.shot, self.user, self.script)

        if self.script == 'NEW.NK':
            print 'Dont need to open anything just set vars and enable stuff'
            jeeves_core.setVars.setJob(self.job)
            jeeves_core.setVars.setShot(self.shot)
 
            nukePipe.jeevesConnectUtils.enablemenus()
            #prompt to save now if there is contents in the current script
        
        else:
            if not os.path.isfile(self.fullpath):
                print 'no file'
                return
            jeeves_core.setVars.setJob(self.job)
            jeeves_core.setVars.setShot(self.shot)
            jeeves_core.setVars.setScript(self.script)
            jeeves_core.setVars.setFullpath(self.fullpath)
            #self.enablemenus()
            nukePipe.jeevesConnectUtils.enablemenus()
            #save current scrpt if not root or untitled and open target script

            nuke.scriptClear()
            nuke.scriptOpen(self.fullpath)

    def changeShot(self, shot):
        print 'CHANGING SHOT'
        
        #clearout
        self.scriptscombo.clear()
        self.allscriptscombo.clear()
        self.shot = None
        self.user = None
        self.script = None
        
        self.job = self.jobsearch.displayText()
        self.user = jeeves_core.user
        self.shot = self.shotcombo.currentText()
        
        self.update_pix()
        
        self.scriptlist = jeeves_core.searchJob.searchMyNukeScripts(self.job, self.shot, self.user)
        
        list(map(self.scriptscombo.addItem, self.scriptlist))
        
        self.allscriptlist = jeeves_core.searchJob.searchAllNukeScripts(self.job, self.shot)
        if self.allscriptlist:
            list(map(self.allscriptscombo.addItem, self.allscriptlist))
 
    def findjob(self):
        print 'FINDING JOB'
        
        #clearout
        self.shotcombo.clear()
        self.scriptscombo.clear()
        self.allscriptscombo.clear()
        self.job = None
        self.shot = None
        self.user = None
        self.script = None
        
        #job
        searchtext = self.jobsearch.displayText()
        self.job = jeeves_core.searchJob.searchJob(searchtext)
        self.jobsearch.setText(self.job)
        
        #shots
        self.shotlist = jeeves_core.searchJob.searchShot(self.job)
        list(map(self.shotcombo.addItem, self.shotlist))
        
        #my scritps
        self.shot = self.shotcombo.currentText()
        self.user = jeeves_core.user
        self.scriptlist = jeeves_core.searchJob.searchMyNukeScripts(self.job, self.shot, self.user)
        list(map(self.scriptscombo.addItem, self.scriptlist))
        
        #all scripts
        self.allscriptlist = jeeves_core.searchJob.searchAllNukeScripts(self.job, self.shot)
        list(map(self.allscriptscombo.addItem, self.allscriptlist))
        
        self.update_pix()

    def update_pix(self):
        shot_pix = os.path.join(jeeves_core.jobsRoot, self.job, 'vfx', 'nuke', self.shot, 'plates', 'tmp', '%s.jpg' % self.shot)
        if os.path.isfile(shot_pix):
            self.lbl.setPixmap(QPixmap(shot_pix).scaled(self.lbl.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        else:
            self.lbl.setPixmap(QPixmap(self.default_pix).scaled(self.lbl.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
        
        
        self.notesfile = os.path.join(jeeves_core.jobsRoot, self.job, 'vfx', 'nuke', self.shot, 'plates', 'tmp', '%s.txt' % self.shot)
        
        if os.path.isfile(self.notesfile):
            f = open(self.notesfile, 'r')
            file_content = f.readlines()
            f.close()
            n = file_content[0]
            self.notes.clear()
            self.notes.insertPlainText(n)
            
        else:
            self.notes.clear()
            

    def checkInstances(self):
        return
        nuke.tprint ('new instance:', self)
        for widget in QApplication.allWidgets():
            name = widget.objectName()
            if 'uk.co.thefoundry.NukeConnectGui' in name:
                nuke.tprint ("instance already present:", self)
                p = widget.parentWidget()
                while p:
                    if p.parent() and isinstance(p.parent(), QStackedWidget):
                        p.parent().removeWidget(p)
                        p = None
                    else:
                        p = p.parentWidget()

def run():
  ## make this work in a .py file and in 'copy and paste' into the script editor
  moduleName = __name__
  if moduleName == '__main__':
    moduleName = ''
  else:
    moduleName = moduleName + '.'

    pane = nuke.getPaneFor('Properties.1')
    panels.registerWidgetAsPanel(moduleName + 'NukeConnectGui', 'Jeeves Connect', 'uk.co.thefoundry.NukeConnectGui', True).addToPane(pane) 
