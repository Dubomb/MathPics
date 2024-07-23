import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:frontend/src/components/widgets/cameradisplay.dart';
import 'package:frontend/src/core/services/imageservice.dart' as imageservice;

class HomePage extends StatelessWidget {
  final CameraDescription camera;

  const HomePage({super.key, required this.camera});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Center(child: Text("MathPics")),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: Column(
        children: [
          CameraDisplay(camera: camera,),
          const Text("Hello!"),
          ElevatedButton(onPressed: () => {
            imageservice.makePrediction(null).then((res) => {print(res)})
          }, child: const Text('Take a picture!')),
        ],
      ),
    );
  }
}