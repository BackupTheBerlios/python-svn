#!/usr/bin/env python
# generated by wxGlade 0.3.2 on Sat Apr 10 23:50:35 2004

####(c)www.stani.be
try:
    import _spe.info as info
except:
    print "SPE path error: the folder of SPE.py should be called '_spe'!"
    print "(Maybe you renamed it to 'spe', please rename it back to '_spe'.)"
    print "SPE will exit now."
    import sys
    sys.exit()

INFO=info.copy()

INFO['description']=\
"""Subclassed smdi frame."""

__doc__=INFO['doc']%INFO

####Modules & constants
import os, wx
import wxgMenu
import sm.wxp.smdi as smdi

STATUS          = "(c) www.stani.be - The name of the current workspace is displayed at the right."

ArtIDs = [ wx.ART_FILE_OPEN,
           wx.ART_PRINT,
           wx.ART_ADD_BOOKMARK,
           wx.ART_REPORT_VIEW,
           wx.ART_LIST_VIEW,
           wx.ART_HELP,
           ]

BLENDER = 4
WINDOW  = 5


TOOLS=[
TOOL_NEW,TOOL_OPEN_FILES, TOOL_SAVE, TOOL_SAVE_AS, TOOL_SAVE_WORKSPACE,
TOOL_REMEMBER_OPEN_FILES,
TOOL_UNDO, TOOL_REDO,
TOOL_FIND__REPLACE, TOOL_GO_TO_LINE, TOOL_BROWSE_SOURCE,
TOOL_INDENT, TOOL_DEDENT, TOOL_COMMENT, TOOL_UNCOMMENT,
TOOL_SIDEBAR, TOOL_SHELL,
TOOL_RUN, TOOL_RUN_DEBUG, TOOL_DEBUG, TOOL_IMPORT,
TOOL_CHECK_SOURCE_WITH_PYCHECKER,
TOOL_LOAD_IN_BLENDER, TOOL_REFERENCE_IN_BLENDER,
TOOL_DONATE
] = \
[wx.NewId() for x in range(25)]

CHILD_TOOLS=[
TOOL_SAVE, TOOL_SAVE_AS, TOOL_SAVE_WORKSPACE,
TOOL_REMEMBER_OPEN_FILES,
TOOL_UNDO, TOOL_REDO,
TOOL_FIND__REPLACE, TOOL_GO_TO_LINE, TOOL_BROWSE_SOURCE,
TOOL_INDENT, TOOL_DEDENT, TOOL_COMMENT, TOOL_UNCOMMENT,
TOOL_SIDEBAR,
TOOL_RUN, TOOL_RUN_DEBUG, TOOL_DEBUG, TOOL_IMPORT,TOOL_CHECK_SOURCE_WITH_PYCHECKER,
]

BLENDER_TOOLS = [TOOL_LOAD_IN_BLENDER, TOOL_REFERENCE_IN_BLENDER]

def _(x):
    if '|' in x and info.DARWIN:
        return x.replace('Ctrl','Cmd').replace('Alt+F4','Cmd+Q')
    else:
        return x

class Tool(wx.ToolBar):
    def __init__(self,parent=None,app=None,id=-1,menu=None,**kwds):
        self.app = app
        wx.Bitmap = app.bitmap
        wx.ToolBar.__init__(self,parent=parent,id=id,**kwds)
        self.SetToolBitmapSize((16,16))
        parent.SetToolBar(self)
        self.AddLabelTool(TOOL_NEW, "", wx.Bitmap("skins/default/filenew.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("New | Ctrl+N"), "")
        self.AddLabelTool(TOOL_OPEN_FILES, "", wx.Bitmap("skins/default/fileopen.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Open files... | Ctrl+O"), "")
        self.AddLabelTool(TOOL_SAVE, "", wx.Bitmap("skins/default/filesave.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Save | Ctrl+S"), "")
        self.AddLabelTool(TOOL_SAVE_AS, "", wx.Bitmap("skins/default/filesaveas.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Save as... | Shift+Ctrl+S"), "")
        self.AddLabelTool(TOOL_SAVE_WORKSPACE, "", wx.Bitmap("skins/default/workspace_save.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Save workspace"), "")
        self.AddLabelTool(TOOL_REMEMBER_OPEN_FILES, "", wx.Bitmap("skins/default/remember.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, _("Remember open files"), "")
        self.AddSeparator()
        self.AddLabelTool(TOOL_UNDO, "", wx.Bitmap("skins/default/undo.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Undo | Ctrl+Z"), "")
        self.AddLabelTool(TOOL_REDO, "", wx.Bitmap("skins/default/redo.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Redo | Ctrl+Y"), "")
        self.AddSeparator()
        self.AddLabelTool(TOOL_FIND__REPLACE, "", wx.Bitmap("skins/default/viewmag.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Find & replace... | Ctrl+F"), "")
        self.AddLabelTool(TOOL_GO_TO_LINE, "", wx.Bitmap("skins/default/goto.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Go to line... | Ctrl+G"), "")
        self.AddLabelTool(TOOL_BROWSE_SOURCE, "", wx.Bitmap("skins/default/thumbnail.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Browse source | Ctrl+Enter"), "")
        self.AddSeparator()
        self.AddLabelTool(TOOL_INDENT, "", wx.Bitmap("skins/default/indent.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Indent | Tab"), "")
        self.AddLabelTool(TOOL_DEDENT, "", wx.Bitmap("skins/default/dedent.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Dedent | Shift+Tab"), "")
        self.AddLabelTool(TOOL_COMMENT, "", wx.Bitmap("skins/default/comment.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Comment | Alt+3"), "")
        self.AddLabelTool(TOOL_UNCOMMENT, "", wx.Bitmap("skins/default/uncomment.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Uncomment | Alt+4"), "")
        self.AddSeparator()
        self.AddLabelTool(TOOL_SIDEBAR, "", wx.Bitmap("skins/default/view_left_right.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, _("View sidebar | F11"), "")
        self.AddLabelTool(TOOL_SHELL, "", wx.Bitmap("skins/default/view_top_bottom.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, _("Show/hide shell | F12"), "")
        self.AddSeparator()
        self.AddLabelTool(TOOL_RUN, "", wx.Bitmap("skins/default/run.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, _("Run.../Stop | F9"), "")
        self.AddLabelTool(TOOL_RUN_DEBUG, "", wx.Bitmap("skins/default/run_debug.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, _("Run/Stop with WinPdb | F9"), "")
        self.AddLabelTool(TOOL_DEBUG, "", wx.Bitmap("skins/default/debug.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Debug with WinPdb... | Ctrl+Shift+D"), "")
        self.AddLabelTool(TOOL_IMPORT, "", wx.Bitmap("skins/default/import.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Import | F10"), "")
        self.AddLabelTool(TOOL_CHECK_SOURCE_WITH_PYCHECKER, "", wx.Bitmap("skins/default/pychecker.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Check source with pychecker | Ctrl+Alt+C"), "")
        self.AddSeparator()
        if app.Blender:
            self.AddLabelTool(TOOL_LOAD_IN_BLENDER, "", wx.Bitmap("skins/default/blender.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Load in Blender | Ctrl+B"), "")
            self.AddLabelTool(TOOL_REFERENCE_IN_BLENDER, "", wx.Bitmap("skins/default/blenderRef.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Reference in Blender | Ctrl+Alt+B"), "")
            self.AddSeparator()
        self.AddLabelTool(TOOL_DONATE, "", wx.Bitmap("skins/default/donate.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Please donate, if you enjoy SPE."), "")
        self.Realize()

    def __events__(self):
        wx.EVT_TOOL(self,TOOL_NEW, self.menuBar.menu_new)
        wx.EVT_TOOL(self,TOOL_OPEN_FILES, self.menuBar.menu_open_files)
        wx.EVT_TOOL(self,TOOL_SAVE, self.menuBar.menu_save)
        wx.EVT_TOOL(self,TOOL_SAVE_AS, self.menuBar.menu_save_as)
        wx.EVT_TOOL(self,TOOL_SAVE_WORKSPACE, self.menuBar.menu_save_workspace)
        wx.EVT_TOOL(self,TOOL_REMEMBER_OPEN_FILES, self.menuBar.menu_remember_open_files)
        #
        wx.EVT_TOOL(self,TOOL_UNDO, self.menuBar.menu_undo)
        wx.EVT_TOOL(self,TOOL_REDO, self.menuBar.menu_redo)
        #
        wx.EVT_TOOL(self,TOOL_FIND__REPLACE, self.menuBar.menu_find__replace)
        wx.EVT_TOOL(self,TOOL_GO_TO_LINE, self.menuBar.menu_go_to_line)
        wx.EVT_TOOL(self,TOOL_BROWSE_SOURCE, self.menuBar.menu_browse_source)
        #
        wx.EVT_TOOL(self,TOOL_INDENT, self.menuBar.menu_indent)
        wx.EVT_TOOL(self,TOOL_DEDENT, self.menuBar.menu_dedent)
        wx.EVT_TOOL(self,TOOL_COMMENT, self.menuBar.menu_comment)
        wx.EVT_TOOL(self,TOOL_UNCOMMENT, self.menuBar.menu_uncomment)
        #
        wx.EVT_TOOL(self,TOOL_SIDEBAR, self.menuBar.menu_sidebar)
        wx.EVT_TOOL(self,TOOL_SHELL, self.menuBar.menu_shell)
        #
        wx.EVT_TOOL(self,TOOL_RUN, self.menuBar.menu_run)
        wx.EVT_TOOL(self,TOOL_RUN_DEBUG, self.menuBar.menu_run_debug)
        wx.EVT_TOOL(self,TOOL_DEBUG, self.menuBar.menu_debug)
        wx.EVT_TOOL(self,TOOL_IMPORT, self.menuBar.menu_import)
        wx.EVT_TOOL(self,TOOL_CHECK_SOURCE_WITH_PYCHECKER, self.menuBar.menu_check_source_with_pychecker)
        #
        if self.app.Blender:
            wx.EVT_TOOL(self,TOOL_LOAD_IN_BLENDER, self.menuBar.menu_load_in_blender)
            wx.EVT_TOOL(self,TOOL_REFERENCE_IN_BLENDER, self.menuBar.menu_reference_in_blender)
        #
        wx.EVT_TOOL(self,TOOL_DONATE, self.menuBar.menu_donate)
        wx.EVT_TOOL_ENTER(self,-1,self.onToolEnter)

    def onToolEnter(self,event):
        if event.GetSelection == -1:
            wx.CallAfter(self.skip,self)

##    def ToggleTool(*arg,**keyw):
##        print arg,keyw
##        wx.ToolBar.ToggleTool(*arg,**keyw)
##
    def skip(self):
        child               = self.app.childActive
        child.statusBar.throbber.Play()

# end of class Tool

class Bar(wxgMenu.Bar):
    #---wxGlade
    def __init__(self, app, frame, *args, **kwds):
        self.app    = app
        self.frame  = frame
        wxgMenu.Bar.__init__(self, *args, **kwds)
        self.CHILD_MENUS = wxgMenu.CHILD_MENUS
        self.CHILD_TOOLS = CHILD_TOOLS
        # Mac  tweaks
        if wx.Platform == "__WXMAC__":
            app.SetMacAboutMenuItemId(wxgMenu.ABOUT)
            app.SetMacPreferencesMenuItemId(wxgMenu.PREFERENCES)
            app.SetMacExitMenuItemId(wx.ID_EXIT)
        #Disable highlight
        self.Bind(wx.EVT_MENU_HIGHLIGHT_ALL,self.skip)

    #---parentPanel
    def enable(self,status):
        if self.toolBar:
            for tool in self.CHILD_TOOLS: self.toolBar.EnableTool(tool,status)
        for menu in self.CHILD_MENUS: self.Enable(menu,status)
        if not self.app.mdi and self.toolBar:
            self.toolBar.EnableTool(TOOL_SHELL,0)
        parentFrame = self.parentFrame
        if hasattr(parentFrame,'palette'):
            parentFrame.palette.enable(status)

    def Bind(self,*arg,**keyw):
        self.frame.Bind(*arg,**keyw)

    def skip(self,event):
        child               = self.app.childActive
        child.statusBar.throbber.Play()

    def link(self,x,doc=None):
        self.parentPanel.messageHtml(x,doc=doc)

    def check_view(self,event=None):
        self.Check(wxgMenu.WHITESPACE, self.parentPanel.getValue('ViewWhiteSpace'))
        self.Check(wxgMenu.INDENTATION_GUIDES, self.parentPanel.getValue('IndentationGuides'))
        self.Check(wxgMenu.RIGHT_EDGE_INDICATOR, self.parentPanel.getValue('ViewEdge'))
        self.Check(wxgMenu.SHELL, self.parentPanel.getValue('ShowShell'))
        #self.Check(wxgMenu.TOOLBAR, self.parentPanel.getValue('ShowToolbar'))
        if self.app.mdi and self.toolBar:
            self.toolBar.ToggleTool(TOOL_SHELL,self.parentPanel.getValue('ShowShell'))
        # TODO: Implement view line numbers and view folding
        #self.Check(LINE_NUMBERS, 1)
        #self.Check(FOLDING, 1)

    def check_sidebar(self,show=True):
        if self.app.childActive:
            self.Check(wxgMenu.SIDEBAR,show)
            if self.toolBar:
                self.toolBar.ToggleTool(TOOL_SIDEBAR,show)

    def check_remember(self,bool):
        self.file.Check(wxgMenu.REMEMBER_OPEN_FILES,bool)
        if self.toolBar:
            self.toolBar.ToggleTool(TOOL_REMEMBER_OPEN_FILES,bool)

    def check_run(self,bool):
        if self.toolBar:
            self.toolBar.ToggleTool(TOOL_RUN,bool)

    def check_run_debug(self,bool):
        if self.toolBar:
            self.toolBar.ToggleTool(TOOL_RUN_DEBUG,bool)

    def check_toolbar(self,show=True):
        if self.toolBar:
            self.parentPanel.set('ShowShell',show)
            self.Check(wxgMenu.TOOLBAR,show)
            if show:
                self.frame.SetToolBar(self.toolBar)
                self.toolBar.Show()
            else:
                self.frame.SetToolBar(None)
                self.toolBar.Destroy()
                self.toolBar = None
                #self.toolBar.Hide()
        if hasattr(self.frame,'sash'):
            wx.LayoutAlgorithm().LayoutMDIFrame(frame)
        else:
            self.frame.Layout()

    #---events
    def __events__(self):
        app = self.app
        #Blender
        if app.Blender:
            self.CHILD_MENUS += wxgMenu.BLENDER_MENUS
            self.CHILD_TOOLS += BLENDER_TOOLS
        else:
            #maybe weird to remove it afterwards but keeps wxGlade intact
            self.Remove(BLENDER)
        if app.mdi not in [smdi.SDI]:#[smdi.MDI_SPLIT,smdi.SDI]:
            self.Remove(WINDOW)
            self.CHILD_MENUS.remove(wxgMenu.NEXT)
            self.CHILD_MENUS.remove(wxgMenu.PREVIOUS)
        #mdi
        if not app.mdi:
            self.Enable(wxgMenu.SHELL,0)
            if self.toolBar:
                self.toolBar.EnableTool(TOOL_SHELL,0)

    def menu_new(self, event=None):
        """File > New"""
        self.parentPanel.new()

    def menu_open_files(self, event=None):
        """File > Open file(s)..."""
        self.parentPanel.open(event)

    def menu_save(self, event=None):
        """File > Save"""
        self.app.childActive.save()
        self.app.parentPanel.save()

    def menu_save_as(self, event=None):
        """File > Save As..."""
        self.app.childActive.saveAs()

    def menu_save_uml_as(self, event=None):
        self.app.childActive.saveUmlAs()

    def menu_save_copy(self, event=None):
        """File > Save a Copy..."""
        self.app.childActive.saveCopy()

    def menu_print_uml(self, event=None):
        self.app.childActive.printUml()

    def menu_print_uml_preview(self, event=None):
        self.app.childActive.printUmlPreview()

    def menu_print_uml_setup(self, event=None):
        self.app.childActive.printUmlSetup()

    def menu_close(self, event=None):
        """File > Close"""
        active = self.app.childActive
        if active:
            active.frame.onFrameClose()

    def menu_exit(self, event=None):
        """File > Exit"""
        self.parentFrame.onFrameClose()

    def menu_remember_open_files(self, event=None):
        """File > Remember open file(s)"""
        self.parentPanel.rememberSet(not self.parentPanel.remember)
        self.Check(wxgMenu.REMEMBER_OPEN_FILES,self.parentPanel.remember)
        if self.toolBar:
            self.toolBar.ToggleTool(TOOL_REMEMBER_OPEN_FILES,self.parentPanel.remember)

    def menu_undo(self, event=None):
        """Edit > Undo"""
        self.app.childActive.source.Undo()

    def menu_redo(self, event=None):
        """Edit > Redo"""
        self.app.childActive.source.Redo()

    def menu_cut(self, event=None):
        """Edit > Cut"""
        self.app.childActive.source.Cut()

    def menu_copy(self, event=None):
        """Edit > Copy"""
        self.app.childActive.source.Copy()

    def menu_paste(self, event=None):
        """Edit > Paste"""
        self.app.childActive.source.Paste()

    def menu_find__replace(self, event=None):
        """Edit > Find & replace..."""
        self.parentPanel.find_replace(event)

    def menu_find_next(self, event=None):
        """Edit > Find next"""
        self.parentPanel.onFind(event)

    def menu_go_to_line(self, event=None):
        """Edit > Go to line..."""
        self.app.childActive.go_to_line()

    def menu_browse_source(self, event=None):
        """Edit > Browse source"""
        self.parentPanel.browse_source()

    def menu_auto_complete(self, event=None):
        """Edit > Auto complete"""
        self.app.childActive.source.autoComplete()

    def menu_show_docstring(self, event=None):
        self.app.childActive.source.showCallTip()

    def menu_indent(self, event=None):
        """Edit > Indent"""
        self.app.childActive.source.CmdKeyExecute(wx.stc.STC_CMD_TAB)

    def menu_dedent(self, event=None):
        """Edit > Dedent"""
        self.app.childActive.source.CmdKeyExecute(wx.stc.STC_CMD_BACKTAB)

    def menu_comment(self, event=None):
        """Edit > Comment"""
        self.app.childActive.comment()

    def menu_uncomment(self, event=None):
        """Edit > UnComment"""
        self.app.childActive.uncomment()

    def menu_insert_separator(self, event=None):
        """Edit > Insert seperator..."""
        self.app.childActive.insert_separator()

    def menu_insert_signature(self, event=None):
        """Edit > Insert seperator..."""
        self.app.childActive.insert_signature()

    def menu_execute(self, event): # wxGlade: Bar.<event_handler>
        """Edit > Execute"""
        self.parentPanel.execute()

    def menu_execute_verbose(self, event): # wxGlade: Bar.<event_handler>
        """Edit > Execute verbose"""
        self.parentPanel.execute_verbose()

    def menu_preferences(self, event=None):
        """Edit > Preferences..."""
        self.parentPanel.preferences()

    def menu_whitespace(self, event=None):
        """View > Whitespace"""
        self.parentPanel.whitespace(event)

    def menu_indentation_guides(self, event=None):
        """View > Indentation guides"""
        self.parentPanel.indentation_guides(event)

    def menu_right_edge_indicator(self, event=None):
        """View > Right edge indicator"""
        self.parentPanel.right_edge_indicator(event)

    def menu_end_of_line_marker(self, event=None):
        """View > End-of-line marker"""
        self.parentPanel.end_of_line_marker(event)

    def menu_as_notebook(self, event):
        self.parentPanel.as_notebook(event)

    def menu_as_columns(self, event):
        self.parentPanel.as_columns(event)

    def menu_as_rows(self, event):
        self.parentPanel.as_rows(event)

    def menu_sidebar(self, event=None):
        """View > Sidebar"""
        self.app.childActive.toggle_sidebar(event)

    def menu_shell(self, event=None):
        """View > Shell"""
        hidden = self.parentPanel.toggle_shell()
        self.Check(wxgMenu.SHELL,hidden)
        if self.toolBar:
            self.toolBar.ToggleTool(TOOL_SHELL,hidden)

    def menu_clear_output(self, event=None):
        """View > Refresh"""
        self.parentPanel.output.Clear()

    def menu_refresh(self, event=None):
        """View > Refresh"""
        self.app.childActive.refresh()

    def menu_toolbar(self, event):
        show = not self.parentPanel.getValue('ShowToolbar')
        self.check_toolbar(show)

    def menu_browse_folder(self, event=None):
        """Tools > Browse folder"""
        self.parentPanel.browse_folder()

    def menu_run(self, event): # wxGlade: Bar.<event_handler>
        self.app.parentPanel.run()

    def menu_run_without_arguments(self, event): # wxGlade: Bar.<event_handler>
        self.app.parentPanel.run_with_arguments()

    def menu_run_terminal(self, event=None):
        """Tools > Run"""
        self.app.childActive.run()

    def menu_run_terminal_without_arguments(self, event):
        self.app.childActive.run_with_arguments(exit=False)

    def menu_run_terminal_without_arguments_exit(self,event):
        self.app.childActive.run_with_arguments(exit=True)

    def menu_run_debug(self, event): # wxGlade: Bar.<event_handler>
        self.parentPanel.run_debug()

    def menu_import(self, event=None):
        """Tools > Import"""
        self.parentPanel.import_()

    def menu_debug(self, event=None):
        """Tools > Import"""
        self.parentPanel.debug()

    def menu_browse_object_with_pyfilling(self, event=None):
        """Tools > Browse object with PyFilling..."""
        self.parentPanel.browse_object_with_pyfilling()

    def menu_test_regular_expression_with_kiki(self, event=None):
        """Tools > Test regular expression with Kiki..."""
        self.parentPanel.test_regular_expression_with_kiki()

    def menu_design_a_gui_with_wxglade(self, event=None):
        """Tools > Design a gui with wxGlade..."""
        self.parentPanel.design_a_gui_with_wxglade()

    def menu_design_a_gui_with_xrc(self, event=None):
        """Tools > Design a gui with XRC..."""
        self.parentPanel.design_a_gui_with_xrc()

    def menu_check_source_with_pychecker(self, event=None):
        """Tools > Check source with PyChecker"""
        self.app.childActive.check_source_with_pychecker()

    def menu_open_terminal_emulator(self, event=None):
        """Tools > Open terminal emulator..."""
        self.app.childActive.open_terminal_emulator()

    def menu_run_in_terminal_emulator(self, event=None):
        """Tools > Run in terminal emulator..."""
        self.app.childActive.run_in_terminal_emulator()

    def menu_run_in_terminal_emulator__exit(self, event=None):
        """Tools > Run in terminal emulator & exit..."""
        self.app.childActive.run_in_terminal_emulator_exit()

    def menu_load_in_blender(self, event=None):
        """Blender > Load in blender"""
        self.app.childActive.load_in_blender()

    def menu_reference_in_blender(self, event=None):
        """Blender > Reference in Blender"""
        self.app.childActive.reference_in_blender()

    def menu_redraw_blender_window(self, event=None):
        """Blender > Redraw blender window"""
        self.app.childActive.refresh()

    def menu_blender_python_manual(self, event=None):
        """Blender > Blender python manual..."""
        self.link('http://spe.stani.be/manual/blender/frames.html')

    def menu_blender_python_tutorial(self, event=None):
        """Blender > Blender python tutorial..."""
        self.link('http://jmsoler.free.fr/didacticiel/blender/tutor/english/index_prog_python.htm')

    def menu_blender_homepage(self, event=None):
        """Blender > Blender homepage..."""
        self.link('http://www.blender.org')

    def menu_download_blender(self, event=None):
        """Blender > Download blender..."""
        self.link('http://www.blender3d.org/Download/')

    def menu_forum_blender_python(self, event=None):
        """Blender > Forum blender python..."""
        self.link('http://www.blender.org/modules.php?op=modload&name=phpBB2&file=viewforum&f=9')

    def menu_forum_elysiun_python(self, event=None):
        """Blender > Forum elYsiun python..."""
        self.link('http://www.elysiun.com/forum/viewforum.php?f=5&sid=1fcd71798ef503d8b093d597d1da142a')

    def menu_spe_homepage(self, event=None):
        """Links > Spe homepage..."""
        self.link('http://pythonide.stani.be')

    def menu_forum_spe(self, event=None):
        """Links > Forum spe..."""
        self.link('http://www.stani.be/python/spe/page_forum')

    def menu_authors_homepage(self, event=None):
        """Links > Authors homepage"""
        self.link('http://www.stani.be')

    def menu_contact_author(self, event=None):
        """Links > Contact author..."""
        self.parentPanel.contact_author()

    def menu_python_homepage(self, event=None):
        """Links > Python homepage..."""
        self.link('http://www.python.org')

    def menu_active_python_distribution(self, event=None):
        """Links > Active python distribution..."""
        self.link('http://www.activestate.com')

    def menu_enthought_python_distribution(self, event=None):
        """Links > Enthought python distribution..."""
        self.link('http://www.enthought.com/python/')

    def menu_python_announcements(self, event=None):
        """Links > Python announcements..."""
        self.link('http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&group=comp.lang.python.announce')

    def menu_python_cookbook(self, event=None):
        """Links > Python cookbook..."""
        self.link('http://www.activestate.com/ASPN/Cookbook/Python')

    def menu_python_daily(self, event=None):
        """Links > Python daily..."""
        self.link('http://www.pythonware.com/daily/')

    def menu_python_for_artists(self, event=None):
        """Links > Python for artists..."""
        self.link('http://spe.pycs.net/stories/6.html')

    def menu_python_package_index(self, event=None):
        """Links > Python package index..."""
        self.link('http://www.python.org/pypi')

    def menu_next(self, event=None):
        """Window > Next"""
        if self.app.mdi:
            self.parentFrame.ActivateNext()
        else: event.Skip()

    def menu_previous(self, event=None):
        """Window > Previous"""
        if self.app.mdi:
            self.parentFrame.ActivatePrevious()
        else: event.Skip()

    def menu_manual(self, event=None):
        """Help > Manual..."""
        self.link('http://pythonide.stani.be/manual/html/manual.html')

    def menu_keyboard_shortcuts(self, event=None):
        """Help > Keyboard shortcuts..."""
        self.link('http://pythonide.stani.be/manual/html/manual12.html')

    def menu_python_library(self, event=None):
        """Help > Python library..."""
        self.parentPanel.python_help('lib')

    def menu_python_reference(self, event=None):
        """Help > Python reference..."""
        self.parentPanel.python_help('ref')

    def menu_python_documentation_server(self, event=None):
        """Help > Python documentation server..."""
        self.parentPanel.python_documentation_server()

    def menu_wxglade_manual(self, event=None):
        """Help > wxGlade manual..."""
        self.link("http://spe.stani.be/manual/wxGlade/index.html")

    def menu_wxglade_tutorial(self, event=None):
        """Help > wxGlade tutorial..."""
        self.link("http://spe.stani.be/manual/wxGlade/tutorial.html")

    def menu_wxwindows_documentation(self, event=None):
        """Help > wxWindows documentation..."""
        self.parentPanel.wxwindows_documentation()

    def menu_donate(self, event=None):
        """Help > Donate..."""
        self.parentPanel.messageHtml('donate.html',doc=self.parentPanel.path)

    def menu_about(self, event=None):
        """Help > About..."""
        if wx.Platform == "__WXMAC__":
            wx.MessageBox("Stani's Python Editor: A Python IDE built on the wxPython toolkit.\n(c)www.stani.be")
        else:
            self.parentPanel.about()

    def menu_open_workspace(self, event):
        self.parentPanel.open_workspace()
        event.Skip()

    def menu_save_workspace(self, event):
        self.parentPanel.save_workspace()
        event.Skip()

    def menu_save_workspace_as(self, event):
        self.parentPanel.save_workspace_as()
        event.Skip()

class PalettePanel(wxgMenu.Palette):
    def evt_indent(self, event):
        self.menuBar.menu_indent()
        self.app.childActive.source.SetFocus()

    def evt_dedent(self, event):
        self.menuBar.menu_dedent()
        self.app.childActive.source.SetFocus()

    def evt_comment(self, event):
        self.menuBar.menu_comment()
        self.app.childActive.source.SetFocus()

    def evt_uncomment(self, event):
        self.menuBar.menu_uncomment()
        self.app.childActive.source.SetFocus()

    def evt_run(self, event):
        self.menuBar.menu_run()

    def evt_import(self, event):
        self.menuBar.menu_import()

    def evt_find(self, event):
        self.menuBar.menu_find__replace()
        self.app.childActive.source.SetFocus()

    def evt_goto(self, event):
        self.menuBar.menu_go_to_line()
        self.app.childActive.source.SetFocus()

    def evt_browse_source(self, event):
        self.menuBar.menu_browse_source()
        self.app.childActive.source.SetFocus()

    def evt_shell(self, event):
        self.menuBar.menu_shell()

    def evt_check(self, event):
        self.menuBar.menu_check_source_with_pychecker()
        self.app.childActive.source.SetFocus()

    def evt_donate(self, event):
        self.menuBar.menu_donate()
        self.app.childActive.source.SetFocus()

    def evt_next(self, event):
        self.menuBar.menu_next()
        self.app.childActive.source.SetFocus()

    def evt_previous(self, event):
        self.menuBar.menu_previous()
        self.app.childActive.source.SetFocus()

    def evt_sidebar(self, event):
        self.menuBar.menu_sidebar()
        self.app.childActive.source.SetFocus()

    def evt_run_verbose(self, event):
        self.menuBar.menu_run_verbose()

class Palette(wx.MiniFrame):
    def __init__(self,parent,*args,**keyw):
        wx.MiniFrame.__init__(self,parent,style=wx.CAPTION|wx.FRAME_FLOAT_ON_PARENT,*args,**keyw)
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        self.panel  = PalettePanel(parent=self,id=wx.ID_ANY)
        sizer_main.Add(self.panel, 0, wx.ADJUST_MINSIZE, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_main)
        sizer_main.Fit(self)
        sizer_main.SetSizeHints(self)

    def enable(self,status):
        for child in self.panel.GetChildren()[:-2]:
            child.Enable(status)

from wx.animate import GIFAnimationCtrl

class Status(wx.StatusBar):
    def __init__(self,parent=None,id=-1):
        wx.StatusBar.__init__(self,parent=parent,id=id)
        self.SetFieldsCount(5)
        self.SetStatusWidths([20, -1, 90, 90, 100])
        self.throbber   = Throbber(self,'throbber_still.gif')
        self.throbber.Play()
        self.SetStatusText(STATUS,1)

class Throbber(GIFAnimationCtrl):
    def __init__(self,statusBar,fileName,position=0):
        GIFAnimationCtrl.__init__(self,statusBar,-1,info.imageFile(fileName))
        self._statusBar = statusBar
        self._fileName  = fileName
        self._position  = position
        self._running   = False
        #backgroundcolour
        player          = self.GetPlayer()
        player.UseBackgroundColour(True)
        #position
        rect            = statusBar.GetFieldRect(0)
        self.SetPosition((rect.x+(rect.width-16)/2, rect.y+(rect.height-16)/2))

    def LoadFile(self,fileName):
        if (hasattr(self,'_fileName') and fileName != self._fileName) and not self._running:
            GIFAnimationCtrl.LoadFile(self,info.imageFile(fileName))
            self._fileName  = fileName
            return True
        return False

    def run(self):
        self.playFile('throbber.gif')
        self._running   = True

    def stop(self):
        self._running   = False
        self.playFile('throbber_still.gif')
        #wx.FutureCall(1000,self.Stop)

    def playFile(self,fileName):
        self.LoadFile(fileName)
        self.Play()
