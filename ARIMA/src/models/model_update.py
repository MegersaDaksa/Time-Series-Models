def update_model_with_new_data(existing_model, new_data):
    model_updated = existing_model.append(new_data)
    model_updated_fit = model_updated.fit()
    return model_updated_fit
