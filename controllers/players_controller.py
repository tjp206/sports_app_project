from flask import Blueprint, Flask, render_template, redirect, request
from models.player import Player
import repositories.player_repo as player_repo