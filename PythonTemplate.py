import sys  # sys is a fundamental Python library - here, we're using it to load in
import clr  # This is .NET's Common Language Runtime. It's an execution environment

clr.AddReference("RevitNodes")  # Dynamo's nodes for Revit
import Revit  # Loads in the Revit namespace in RevitNodes
clr.ImportExtensions(Revit.Elements)  # More loading of Dynamo's Revit libraries

clr.AddReference("RevitServices")  # Dynamo's classes for handling Revit documents
import RevitServices
from RevitServices.Persistence import DocumentManager  # An internal Dynamo class, that keeps track of the document that
# Dynamo is currently attached to
from RevitServices.Transactions import TransactionManager  # A Dynamo class for opening and closing transactions to
# change the Revit document's database

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

doc = DocumentManager.Instance.CurrentDBDocument  # Finally, setting up handles to the active Revit document
uiapp = DocumentManager.Instance.CurrentUIApplication  # Setting a handle to the active Revit UI document

# #######OK NOW YOU CAN CODE####### #
