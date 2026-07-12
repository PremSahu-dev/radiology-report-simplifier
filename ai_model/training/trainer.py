"""
trainer.py

Trainer class for model training.
"""

import torch
from training.metrics import calculate_metrics
from training.checkpoint import save_checkpoint

class Trainer:

    def __init__(
        self,
        model,
        train_loader,
        optimizer,
        criterion,
        scheduler,
        device
    ):
        """
        Initializes the trainer.
        """

        self.model = model
        self.train_loader = train_loader

        self.optimizer = optimizer
        self.criterion = criterion
        self.scheduler = scheduler

        self.device = device

        self.model.to(self.device)

        # Training State
        self.best_accuracy = -1.0
        self.current_epoch = 0

        # History
        self.train_loss_history = []
        self.train_metric_history = []
        

    def train_one_epoch(self):
        """
        Trains the model for one epoch.
        """

        self.model.train()

        running_loss = 0.0

        all_predictions = []

        all_labels = []

        for images, labels in self.train_loader:

            images = images.to(self.device)

            labels = labels.to(self.device)

            # Clear previous gradients
            self.optimizer.zero_grad()

            # Forward pass
            outputs = self.model(images)

            # Calculate loss
            loss = self.criterion(outputs, labels)

            # Backpropagation
            loss.backward()

            # Update model weights
            self.optimizer.step()

            running_loss += loss.item()

            # Predicted class
            predictions = torch.argmax(outputs, dim=1)
            

            all_predictions.extend(
                predictions.cpu().numpy().tolist()
            )

            all_labels.extend(
                labels.cpu().numpy().tolist()
            )

        average_loss = running_loss / len(self.train_loader)

        return average_loss, all_labels, all_predictions
        
       
       
    def fit(self, epochs):
        """
        Trains the model for multiple epochs.
        """

        for epoch in range(epochs):

            self.current_epoch = epoch + 1

            loss, labels, predictions = self.train_one_epoch()

            metrics = calculate_metrics(
                labels,
                predictions
            )

            self.train_loss_history.append(loss)

            self.train_metric_history.append(metrics)

            print(f"\nEpoch {self.current_epoch}/{epochs}")
            print("-" * 30)
            print(f"Loss      : {loss:.4f}")
            print(f"Accuracy  : {metrics['accuracy']:.4f}")
            print(f"Precision : {metrics['precision']:.4f}")
            print(f"Recall    : {metrics['recall']:.4f}")
            print(f"F1 Score  : {metrics['f1_score']:.4f}")
            
            # Save best model
            if metrics["accuracy"] > self.best_accuracy:

                self.best_accuracy = metrics["accuracy"]  

                save_checkpoint(
                 model=self.model,
                 filepath="../checkpoints/best_mri_model.pth"
                )

                print("✅ Best model saved.") 	

            self.scheduler.step()  
            print()
                  
        
   

    
