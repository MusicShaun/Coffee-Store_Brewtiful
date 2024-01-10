
          
<!-- Adding quantity processing   -->
  <form action="{{ url_for('views.checkout') }}" method="POST" id="updateForm_{{ item.name }}">
    <input type="number" name="quantity" value="{{ item.quantity }}" min="1" max="25" class="update-input" onchange="updateCartQuantity(this.form, '{{ item.name }}', this.value)">
  </form> -->
  <td>${{ (item.price | float) * (item.quantity | int)}}</td>
  <form action="{{ url_for('views.delete_from_cart', product_id=item.name) }}" method="POST">
    <input type="submit" value="X" id="delete-btn" >
  </form>
