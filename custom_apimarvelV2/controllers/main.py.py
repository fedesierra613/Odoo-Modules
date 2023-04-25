from odoo import http
from odoo.http import request
import requests
from .models.marvel_character import MarvelCharacter
import hashlib
import time


class MarvelCharacterController(http.Controller):

    @http.route('/marvel_characters', auth='public', website=True)
    def marvel_characters(self, **kw):

        timestamp = str(time.time())
        private_key = 'e3392d9dc429cf98e990d365c347b3559a81c89a'
        public_key = '104ac38eb4c8072a1d4136dcb0ea2f5c'
        to_hash = timestamp + private_key + public_key
        hash = hashlib.md5(to_hash.encode()).hexdigest()

        url = 'https://gateway.marvel.com/v1/public/characters'
        params = {'apikey': public_key, 'ts': timestamp, 'hash': hash}
        response = requests.get(url, params=params).json()
        characters = response.get('data').get('results')
        for character in characters:
            name = character.get('name')
            description = character.get('description')
            thumbnail = character.get('thumbnail').get(
                'path') + '.' + character.get('thumbnail').get('extension')
            request.env['marvel.character'].sudo().create(
                {'name': name, 'description': description, 'thumbnail': thumbnail})
        return http.request.render('custom_apimarvel.marvel_character_template', {})
