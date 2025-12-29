from odoo import models, fields , api
import os
from openai import OpenAI


class Laptop(models.Model):
    _name = 'laptop'
    _description = 'Laptop'

    name = fields.Char(string='Name')
    brand = fields.Char(string='Brand')
    model = fields.Char(string='Model')
    price = fields.Float(string='Price')

    ai_comment = fields.Text(string='AI Comment')
    ai_suggestion = fields.Text(string='AI Suggestion')

    is_ai_used = fields.Boolean('is_ai_used', default=False)

    # @api.onchange('name')
    # def _ai_agent(self):
    #     if self.name:
    #         print("AI Agent Triggered")
    #         system_param = self.env['ir.config_parameter'].get_param('system_prompt')
    #         user_prompt = self.name
    #         value = self.name

    #         if not system_param:
    #             system_param = "You are a helpful assistant that provides comments and suggestions for laptop entries based on their name."

    #         if not user_prompt:
    #             user_prompt = f"Provide a comment and suggestion for the laptop named: {value}."

    #         # user_prompt = user_prompt.replace("[value]", value)
            

    #         client = OpenAI(api_key="API-KEY", base_url="https://api.deepseek.com")

    #         response = client.chat.completions.create(
    #             model="deepseek-chat",
    #             messages=[
    #                 {"role": "system", "content": system_param},
    #                 {"role": "user", "content": f"check if this prompt is appropriate,if its talking about killing and sex and other bad stuff its unappropriate {user_prompt} , and only reply yes or no"},
    #             ],
    #             stream=False
    #         )

    #         print("Appropriateness Check Response:", response.choices[0].message.content)

    #         if "no" in str(response.choices[0].message.content).lower():
    #             self.ai_comment = "The provided laptop name is not appropriate."
    #             self.ai_suggestion = "Please provide a valid laptop name."
    #             self.is_ai_used = True
    #             return

    #         response = client.chat.completions.create(
    #             model="deepseek-chat",
    #             messages=[
    #                 {"role": "system", "content": system_param},
    #                 {"role": "user", "content": f" give me comment on, {user_prompt}"},
    #             ],
    #             stream=False
    #         )

    #         self.ai_comment = str(response.choices[0].message.content)

    #         response = client.chat.completions.create(
    #             model="deepseek-chat",
    #             messages=[
    #                 {"role": "system", "content": system_param},
    #                 {"role": "user", "content": f" give me suggestion on, {user_prompt}"},
    #             ],
    #             stream=False
    #         )

    #         self.ai_suggestion = str(response.choices[0].message.content)

    #         self.is_ai_used = True


    def _ai_agent_api(self,user_prompt,system_prompt):
        API_KEY = self.env['ir.config_parameter'].get_param('ai_key')
        client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=False
        )

        return str(response.choices[0].message.content)


    def ai_agent_check_appropriateness(self,value,system_prompt):
        user_prompt = self.env['ir.config_parameter'].get_param('ai_appropriate')
        if not user_prompt:
            return False
        # system_prompt = self.env['ir.config_parameter'].get_param('system_prompt')

        user_prompt = user_prompt.replace("[value]", value)    
        ai_response = self._ai_agent_api(user_prompt,system_prompt)
        if ai_response.lower().strip() == "yes":
            return True
        return False

    def ai_agent_generate_comment_suggestion(self,value,system_prompt,option):
        user_prompt = self.env['ir.config_parameter'].get_param('user_prompt')
        if not user_prompt:
            return False

        user_prompt = user_prompt.replace("[value]", value)
        user_prompt = user_prompt.replace("[option]", option)

        ai_response = self._ai_agent_api(user_prompt,system_prompt)
        return str(ai_response)


    
    def _generate_ai_response(self,value):
        if value:
            system_prompt = self.env['ir.config_parameter'].get_param('system_prompt')
            if not system_prompt:
                return False

            is_appropriate = self.ai_agent_check_appropriateness(value, system_prompt)
            if not is_appropriate:
                self.ai_comment = "The provided laptop name is not appropriate."
                self.ai_suggestion = "Please provide a valid laptop name."
                self.is_ai_used = True
                return

            comment = self.ai_agent_generate_comment_suggestion(value, system_prompt, "comment")
            suggestion = self.ai_agent_generate_comment_suggestion(value, system_prompt, "suggestion")

            self.ai_comment = comment
            self.ai_suggestion = suggestion
            self.is_ai_used = True


    @api.onchange('name')
    def _ai_agent(self):
        self._generate_ai_response(value=self.name)


        