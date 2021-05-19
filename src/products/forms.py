from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

class RawProductForm(forms.Form):
	title       = forms.CharField(label='', widget=forms.TextInput(
														attrs={
															"id": "my-cool-id",
															"placeholder": "Your title"
														}
													)
												)
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
									attrs={
										"class": "new-class-name asdsada",
										"id": "my-id-for-textarea",
										"placeholder": "Your description",
										"rows": 5,
										"cols": 120
									}
								)
							)
	price       = forms.DecimalField(initial=199.99)