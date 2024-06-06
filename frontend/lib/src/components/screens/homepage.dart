import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Center(child: Text("MathPics")),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: const Text("Hello!"),
    );
  }
}