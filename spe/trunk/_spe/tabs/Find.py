#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4cvs on Thu Jul 07 12:43:06 2005

####(c)www.stani.be-------------------------------------------------------------

import _spe.info
INFO=_spe.info.copy()

INFO['description']=\
"""This a demonstration of how to make a tab plugin for spe with wxGlade:
Just design a wxPanel and send it to s_t_a_n_i@yahoo.com

This tab uses the FindReplaceEngine, copyrighted by Tim Hochberg."""

__doc__=INFO['doc']%INFO

####wxGlade---------------------------------------------------------------------

import wx

class wxgPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxgPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.results = wx.Notebook(self, -1, style=wx.NB_BOTTOM)
        self.find = wx.Button(self, -1, "Find in files")
        self.clear = wx.Button(self, -1, "Clear Results")
        self.patternLabel = wx.StaticText(self, -1, "What")
        self.pattern = wx.TextCtrl(self, -1, "")
        self.pathLabel = wx.StaticText(self, -1, "Path")
        self.path = wx.TextCtrl(self, -1, "")
        self.browse = wx.BitmapButton(self, -1, wx.NullBitmap)
        self.pathDepthLabel = wx.StaticText(self, -1, "Path depth")
        self.pathDepth = wx.SpinCtrl(self, -1, "5", min=0, max=100)
        self.label_16 = wx.StaticText(self, -1, "Extensions")
        self.extensions = wx.TextCtrl(self, -1, ".py,.pyw")
        self.case = wx.CheckBox(self, -1, "Match case")
        self.wildcards = wx.CheckBox(self, -1, "Wildcards")
        self.word = wx.CheckBox(self, -1, "Whole words")
        self.regex = wx.CheckBox(self, -1, "Regular expressions")
        self.text_ctrl_1 = wx.TextCtrl(self.results, -1, "Tip: Leave the 'Path' field empty to search in all open files.\n\nBesides from being usefull, this tab is an example how to extend spe with wxGlade. Just design a panel (or frame) and send it to s_t_a_n_i@yahoo.com Than I'll integrate in the next spe release. For more information see in spe/tabs the files Find.wxg (open in wxGlade) and spe/tabs/Find.py (open in spe).", style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxgPanel.__set_properties
        self.SetMinSize((706, 290))
        self.pattern.SetMinSize((178, -1))
        self.browse.SetMinSize((23, 23))
        self.pathDepth.SetMinSize((178, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxgPanel.__do_layout
        sizerHor = wx.BoxSizer(wx.HORIZONTAL)
        sizerVerForm = wx.BoxSizer(wx.VERTICAL)
        sizerFGoptions = wx.FlexGridSizer(2, 2, 4, 4)
        sizerFGfields = wx.FlexGridSizer(4, 2, 4, 4)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizerFGfields.Add(self.find, 0, 0, 0)
        sizerFGfields.Add(self.clear, 0, wx.FIXED_MINSIZE, 0)
        sizerFGfields.Add(self.patternLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizerFGfields.Add(self.pattern, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        sizerFGfields.Add(self.pathLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10.Add(self.path, 1, 0, 0)
        sizer_10.Add(self.browse, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizerFGfields.Add(sizer_10, 0, wx.EXPAND, 0)
        sizerFGfields.Add(self.pathDepthLabel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizerFGfields.Add(self.pathDepth, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        sizerFGfields.Add(self.label_16, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizerFGfields.Add(self.extensions, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0)
        sizerFGfields.AddGrowableCol(1)
        sizerVerForm.Add(sizerFGfields, 0, wx.EXPAND, 0)
        sizerFGoptions.Add(self.case, 0, 0, 2)
        sizerFGoptions.Add(self.wildcards, 0, 0, 2)
        sizerFGoptions.Add(self.word, 0, 0, 2)
        sizerFGoptions.Add(self.regex, 0, 0, 2)
        sizerVerForm.Add(sizerFGoptions, 0, wx.TOP, 4)
        sizerHor.Add(sizerVerForm, 0, wx.ALL|wx.EXPAND, 4)
        self.results.AddPage(self.text_ctrl_1, "Results")
        sizerHor.Add(self.results, 1, wx.ALL|wx.EXPAND, 4)
        self.SetAutoLayout(True)
        self.SetSizer(sizerHor)
        # end wxGlade

# end of class wxgPanel

####Custom----------------------------------------------------------------------

import os,sm.osx
import _spe.help

class Panel(wxgPanel):
    """

    wildcards?
    """
    #---constructor
    def __init__(self, panel, *args, **kwds):
        wxgPanel.__init__(self,parent=panel,id=-1)
        self.panel = panel
        self.browse.SetBitmapLabel(panel.app.bitmap('fileopen.png'))
        self.used=0
        self.data=[]
        self.SetHelpText(_spe.help.FIND)
        self.browse.Bind(wx.EVT_BUTTON, self.onBrowseButton)
        self.find.Bind(wx.EVT_BUTTON, self.onFindButton)
        self.clear.Bind(wx.EVT_BUTTON, self.onClearButton)
        self.pattern.Bind(wx.EVT_TEXT_ENTER,self.onFindButton)

    #---events
    def onBrowseButton(self,event):
        """When browse is clicked, show dir select dialog."""
        #try:
        path    = os.path.dirname(self.panel.app.childActive.fileName)
        #except:
        #    path    = self.path.GetValue()
        dlg         = wx.DirDialog(self,defaultPath=path)
        if dlg.ShowModal() == wx.ID_OK:
            dir     = dlg.GetPath()
            self.path.SetValue(dir)
        dlg.Destroy()

    def onFindButton(self,event):
        #get values
        pattern     = self.pattern.GetValue()
        path        = self.path.GetValue()
        extensions  = self.extensions.GetValue().split(',')
        pathDepth   = self.pathDepth.GetValue()
        case        = self.case.GetValue()
        word        = self.word.GetValue()
        regex       = self.regex.GetValue()

        self.panel.SetStatusText('Collecting filenames ...')
        engine      = FindReplace(case=case, word=word, regex=regex, wrap=1, reverse=0)
        if path:
            names   = sm.osx.listdirR(path,pathDepth,extensions)
        else:
            names   = self.panel.getFileNames()
        results     = engine.findAllInFiles(names,self,pattern,path=path)

    #---Clear Results Event added by Sam Widmer
    def onClearButton(self,event):
        if self.results.GetPageCount() > 1:
            curpage = self.results.GetSelection()
            self.results.RemovePage(curpage)
        else:
            self.results.RemovePage(0)
            txtctl = wx.TextCtrl(self.results, -1, "", style = wx.TE_MULTILINE)
            self.results.AddPage(txtctl, "Results")
            
        
    def onEntrySelect(self,event):
        file,line,col=self.data[event.GetData()]
        self.panel.openList(file,line-1,col)

    #---methods
    def add(self,pattern, results):
        report=wx.ListCtrl(self.results, -1, style=wx.LC_REPORT)
        report.InsertColumn(0,"File")
        report.SetColumnWidth(0, 150)
        report.InsertColumn(1,"Line")
        report.SetColumnWidth(1, 50)
        report.InsertColumn(2,"Col")
        report.SetColumnWidth(2, 50)
        report.InsertColumn(3,"Text")
        report.SetColumnWidth(3, 600)
        report.InsertColumn(4,"Path")
        report.SetColumnWidth(4, 300)
        row=0
        for filename, entries in results.items():
            for entry in entries:
                line,col,text   = entry
                col            -= 1
                path,base       = os.path.split(filename)
                item            = report.InsertStringItem(row,base)
                report.SetStringItem(row,1,str(line))
                report.SetStringItem(row,2,str(col))
                report.SetStringItem(row,3,text)
                report.SetStringItem(row,4,path)
                report.SetItemData(item,len(self.data))
                self.data.append((filename,line,col))
                row            += 1
        if not self.used:
            self.results.DeletePage(0)
            self.used=1
        wx.EVT_LIST_ITEM_SELECTED(report,-1,self.onEntrySelect)
        self.results.InsertPage(0,report, pattern, select=1)
        self.results.Refresh()
        self.results.SetSelection(0)
        self.panel.SetStatusText('"%s" was found %s times in %s files.'%(pattern,row,len(results)))

# end of class Panel

####FindReplaceEngine by Tim Hochberg-------------------------------------------

#-----------------------------------------------------------------------------
# Name:        FindReplaceEngine.py
# Purpose:
#
# Author:      Tim Hochberg
#
# Created:     2001/29/08
# Changed:     2003/10/02 by www.stani.be to pass values by __init__
# RCS-ID:      $Id: FindReplaceEngine.py,v 1.5 2003/01/03 01:46:12 riaan Exp $
# Copyright:   (c) 2001 Tim Hochberg
# Licence:     GPL
#-----------------------------------------------------------------------------
import re, string

class FindError(ValueError):
    pass

def _fix(match, offset, length, selectionStart):
    if match is None:
        return None
    r = []
    try:
        for i in match.span():
            r.append((i + offset) % length + selectionStart)
    except:pass
    return tuple(r)

class FindReplaceEngine:
    def __init__(self, case=0, word=0, regex=0, wrap=1, wildcard=0, reverse=0):
        self.case = case
        self.word = word
        if regex:
            self.mode       = 'regex'
        elif wildcard:
            self.mode       = 'wildcard' # or wildcard or regex
        else:
            self.mode       = 'text' # or wildcard or regex
        self.wrap           = wrap
        self.closeOnFound   = 0
        self.reverse        = reverse
        self.selection      = 0
        self.findHistory    = ['']
        self.replaceHistory = ['']
        self.folderHistory  = ['']
        self.suffixHistory  = ['*.py']
        self.suffixes       = [".py"]
        self.regions        = {}
        self.loadOptions()

    def _addHistory(self, pattern, history):
        if pattern:
            if pattern in history:
                history.remove(pattern)
            history.append(pattern)

    def addFind(self, pattern):
        self._addHistory(pattern, self.findHistory)

    def addReplace(self, pattern):
        self._addHistory(pattern, self.replaceHistory)

    def addFolder(self, pattern):
        self._addHistory(pattern, self.folderHistory)

    def addSuffix(self, pattern):
        self._addHistory(pattern, self.suffixHistory)

    def setRegion(self, view, region):
        self.regions[view] = region

    def getRegion(self, view):
        region = self.regions.get(view, view.GetSelection())
        if region[0] == region[1]:
            region = (0, view.GetTextLength())
        return region

    def findInSource(self, view, pattern):
        region = self.getRegion(view)
        self.addFind(pattern)
        start = view.GetSelection()[not self.reverse]
        if self.selection:
            result = self._find(apply(view.GetTextRange, region), pattern, start, region[0])
        else:
            result = self._find(view.GetText(), pattern, start, 0)
        if result is None:
            raise FindError("'%s' not found" % pattern)
        view.model.editor.addBrowseMarker(view.GetCurrentLine())

        if (result[0] < view.GetCurrentPos() and not self.reverse and self.wrap) or \
           (result[0] > view.GetCurrentPos() and self.reverse and self.wrap):
            view.model.editor.setStatus('Search wrapped', 'Warning', ringBell=1)

        view.SetSelection(result[0], result[1])

    def findNextInSource(self, view):
        self.findInSource(view, self.findHistory[-1])

    def _findAllInSource(self, text, pattern, selectionStart):
        viewResults = []
        for s, e in self._findAll(text, pattern, selectionStart, selectionStart):
            t = text[:s]
            lineNo = string.count(t, '\n')
            left = max(string.rfind(t, '\n'), 0) + 1
            index = s - left
            line = string.split(text[left:], "\n", 1)[0]
            viewResults.append((lineNo+1, index+1, line))
        return viewResults

    def findAllInSource(self, view, pattern):
        region = self.getRegion(view)
        self.addFind(pattern)
        if self.selection:
            results = self._findAllInSource(apply(view.GetTextRange, region), pattern, region[0])
        else:
            results = self._findAllInSource(view.GetText(), pattern, 0)
        name = 'Results: ' + pattern
        if not view.model.views.has_key(name):
            resultView = view.model.editor.addNewView(name, FindResults)
        else:
            resultView = view.model.views[name]
        resultView.tabName = name
        resultView.results = {view.model.filename : results} # XXX should this be viewName?
        resultView.findPattern = pattern
        resultView.refresh()
        resultView.focus()

        resultView.rerunCallback = self.findAllInSource
        resultView.rerunParams = (view, pattern)

    def replaceInSource(self, view, pattern, new):
        region = self.getRegion(view)
        self.addFind(pattern)
        self.addReplace(new)
        # GetSelectedText returns bugus string when nothing is selected
        selRange = view.GetSelection()
        selText = view.GetSelectedText()
        if selRange[0] == selRange[1]:
            selText = ''
        # If the text to be replaced is not yet selected, don't replace, just
        # look for the next occurence.
        if self._find(selText, pattern, 0, 0) is not None: # XXX make more specific
            start = selRange[self.reverse]
            if self.selection:
                result = self._find(apply(view.GetTextRange, region), pattern, start, region[0])
            else:
                result = self._find(view.GetText(), pattern, start, 0)
            if result is None:
                raise FindError("'%s' not found" % pattern)
            view.SetSelection(result[0], result[1])
            compiled = self._compile(pattern)
            if self.mode == 'regex':
                new = compiled.sub(new, view.GetSelectedText())
            view.ReplaceSelection(new)

        # Attempt to find the next replacement
        try:
            self.findInSource(view, pattern)
        except FindError:
            pass

    def replaceAllInSource(self, view, pattern, new):
        region = self.getRegion(view)
        self.addFind(pattern)
        self.addReplace(new)
        text = view.GetText()
        # Replace from the end so that we can do the replace in place without
        # the indices getting messed up.
        self.reverse, oldReverse = 1, self.reverse
        if self.selection:
            results = self._findAll(apply(view.GetTextRange, region), pattern, region[0], region[0])
        else:
            results = self._findAll(view.GetText(), pattern, 0, 0)
        self.reverse = oldReverse
        compiled = self._compile(pattern)
        if results == []:
            return
        view.model.editor.addBrowseMarker(view.GetCurrentLine())
        for item in results:
            view.SetSelection(item[0], item[1])
            n = new
            if self.mode == 'regex':
                n = compiled.sub(new, view.GetSelectedText())
            view.ReplaceSelection(n)
        view.model.editor.statusBar.setHint("%s items replaced" % len(results))

    def findNamesInPackage(self, view):
        names = []
        packages = [os.path.dirname(view.model.assertLocalFile())]
        for base in packages:
            for p in map(lambda n, base=base: os.path.join(base, n), os.listdir(base)):
            #for p in [os.path.join(base, n) for n in os.listdir(base)]: #1.5.2 support
                if os.path.isfile(p) and os.path.splitext(p)[1] in self.suffixes:
                    names.append(p)
                elif os.path.isdir(p) and os.path.isfile(os.path.join(base, "__init__.py")):
                    packages.append(p)
        names.sort(lambda x, y : os.path.basename(x) > os.path.basename(y))
        return names

    def findAllInFiles(self, names, view, pattern):
        self.addFind(pattern)
        results = {}
        # Setup progress dialog
        dlg = wx.ProgressDialog("Finding '%s' in files" % pattern,
                           'Searching...',
                            len(names),
                            view,
                            wx.PD_CAN_ABORT | wx.PD_APP_MODAL | wx.PD_AUTO_HIDE)
        try:

            for i in range(len(names)):
                filename = self._getValidFilename(names[i])
                if not filename: continue
                results[names[i]] = self._findAllInSource(open(filename).read(), pattern, 0)
                if not dlg.Update(i, "Searching in file '%s'"%filename):
                    try:
                        view.model.editor.statusBar.setHint("Search aborted")
                    except:
                        pass

            view.rerunCallback = self.findAllInFiles
            view.rerunParams = (names, view, pattern)

            view.addFindResults(pattern, results)
        finally:
            dlg.Destroy()

    def findAllInPackage(self, view, pattern):
        self.findAllInFiles(self.findNamesInPackage(view), view, pattern)

    def findAllInApp(self, view, pattern):
        names = map(view.model.moduleFilename, view.model.modules.keys())
        names.sort()
        self.findAllInFiles(names, view, pattern)


    def _compile(self, pattern):
        flags = [re.IGNORECASE, 0][self.case]
        if not self.mode == 'regex':
            pattern = re.escape(pattern)
        if self.mode == 'wildcard':
            pattern = pattern.replace(r'\?', '.?')
            pattern = pattern.replace(r'\*', '.*')
        if self.word:
            pattern = r"\b%s\b" % pattern
        return re.compile(pattern, flags)

    def _processText(self, text, start):
        before, after = text[:start], text[start:]
        if self.wrap:
            offset = start
            domain = after + before
        elif not self.reverse:
            offset = start
            domain = after
        else:
            offset = 0
            domain = before
        return domain, offset

    def _findAll(self, text, pattern, start, selectionStart):
        start = start - selectionStart
        compiled = self._compile(pattern)
        domain, offset = self._processText(text, start)
        matches = []
        start = 0
        while 1:
            s = compiled.search(domain, start)
            if s is None or s.end() == 0:
                break
            start = s.end()
            matches.append(_fix(s, offset, len(text), selectionStart))
        if self.reverse:
            matches.reverse()
        return matches

    def _find(self, text, pattern, start, selectionStart):
        if self.reverse:
            return (self._findAll(text, pattern, start, selectionStart) + [None])[0]
        start = start - selectionStart
        compiled = self._compile(pattern)
        domain, offset = self._processText(text, start)
        return _fix(compiled.search(domain), offset, len(text), selectionStart)

    def loadOptions(self):
        pass
##        try:
##            conf = Utils.createAndReadConfig('Explorer')
##            if conf.has_section('finder'):
##                self.wrap = conf.getint('finder', 'wrap')
##                self.closeOnFound = conf.getint('finder', 'closeonfound')
##        except:
##            print 'Problem loading finder options'

    def saveOptions(self):
        pass
##        try:
##            conf = Utils.createAndReadConfig('Explorer')
##            if not conf.has_section('finder'): conf.add_section('finder')
##            conf.set('finder', 'wrap', self.wrap)
##            conf.set('finder', 'closeonfound', self.closeOnFound)
##            Utils.writeConfig(conf)
##        except Exception, err:
##            print 'Problem saving finder options: %s' % err

    def _getValidFilename(self, filename):
        protsplit = string.split(filename, '://')
        if len(protsplit) > 1:
            if protsplit[0] != 'file' or len(protsplit) > 2:
                wx.LogWarning('%s not searched, only local files allowed'%filename)
                return ''
            return protsplit[1]
        return filename

class FindReplace(FindReplaceEngine):
    def findAllInFiles(self, names, view, pattern, path=''):
        self.addFind(pattern)
        results = {}
        # Setup progress dialog
        dlg = wx.ProgressDialog("Finding '%s' in %s" % (pattern,os.path.basename(path)),
                           'Searching...',
                            len(names),
                            view,
                            wx.PD_CAN_ABORT | wx.PD_APP_MODAL | wx.PD_AUTO_HIDE)
        try:

            for i in range(len(names)):
                filename = self._getValidFilename(names[i])
                if not filename and os.path.exists(filename): continue
                results[names[i]] = self._findAllInSource(open(filename).read(), pattern, 0)#(lineNo+1, index+1, line)
                if not dlg.Update(i, "Searching in file '%s'"%filename):
                    try:
                        view.panel.SetStatusText("Search aborted")
                    except:
                        pass

            view.rerunCallback = self.findAllInFiles
            view.rerunParams = (names, view, pattern)

            view.add(pattern, results)
            return results
        finally:
            dlg.Destroy()

    def loadOptions(self):
        pass

    def saveOptions(self):
        pass


if __name__=='__main__':
    import sm.wxp
    sm.wxp.panelApp(Panel)