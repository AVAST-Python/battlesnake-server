from flask import Blueprint, render_template, request, redirect, url_for, flash

user = Blueprint('user', __name__)
from .code import *
from .login import *



